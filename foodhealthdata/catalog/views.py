from django.shortcuts import render
from .models import Food, Nutrient, FoodInstance, User
from django.views import generic, View
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import SignupUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from datetime import date

@login_required
def index(request):

    num_foods = Food.objects.all().count()
    context = {
        'num_foods': num_foods,
    }
    return render(request, 'index.html', context=context)


class FoodListView(LoginRequiredMixin, generic.ListView):
    def post(self, request):
        searched = request.POST.get('searched')
        foods = Food.objects.filter(name__contains=searched)
        context = {'food_list':foods}
        return render(request,'catalog/food_list.html',context=context)
    model = Food
    context_object_name = 'food_list'


class FoodDetailView(LoginRequiredMixin, generic.DetailView):
    model = Food
    #data = serializers.serialize("python", model.objects.all())
    #context_object_name = 'data'
    #context_object_name ='food_item'
    #queryset = Food.objects.get(fdc_id__exact=)
    #vitaminA_rdi = Nutrient.objects.get(name__iregex=r'^'+list(Food.objects.filter(name__icontains='oat').values('vitaminA')[0].items())[0][0][0:-1]+r'.*'+list(Food.objects.filter(name__icontains='oat').values('vitaminA')[0].items())[0][0][-1]).rdi_male_19y_50y

class FoodsEatenByUser(LoginRequiredMixin, generic.ListView):
    model = FoodInstance
    template_name = 'catalog/foodinstance_list_eaten_user.html'
    paginate_by = 100
    def get_queryset(self):
        return (
                FoodInstance.objects.filter(eater=self.request.user).order_by('date').order_by('meal'))

class Signup(generic.CreateView):
    model = User
    form_class = SignupUserForm
    template_name = 'catalog/signup_user.html'
    def get_success_url(self) -> str:
        login(self.request,self.object)
        return reverse('index')
    
class Planner(generic.TemplateView):
    model = Food
    template_name='catalog/planner.html'
    def get(self, request, *args, **kwargs):
        calcium=Food.objects.all().order_by('-calcium')[:10]
        today_food = FoodInstance.objects.filter(eater=request.user).filter(date_eaten=date.today())
        calcium_amt=0
        if today_food:
            for f in today_food:
                if f.fdc_id.calcium:
                    calcium_amt += int(f.fdc_id.calcium)
        context={'calcium':calcium,
                 'calcium_amt':calcium_amt}
        return render(request,'catalog/planner.html',context)
        
    def post(self,request):
        if request.POST.get('calcium'):
            FoodInstance.objects.create(eater=request.user,
                                        fdc_id=Food.objects.get(fdc_id=request.POST.get('fdc_id')),
                                        meal=1,
                                        amount=100)
            context={}
            return render(request,'catalog/planner.html',context)
    


    
