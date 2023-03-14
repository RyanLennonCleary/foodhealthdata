from django.shortcuts import render
from .models import Food, Nutrient, FoodInstance, User
from django.views import generic
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):

    num_foods = Food.objects.all().count()
    context = {
        'num_foods': num_foods,
    }
    return render(request, 'index.html', context=context)


class FoodListView(LoginRequiredMixin, generic.ListView):

    model = Food
    context_object_name = 'food_list'
    queryset = Food.objects.filter(name__contains='kale').order_by('calcium')[:50]
    
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

