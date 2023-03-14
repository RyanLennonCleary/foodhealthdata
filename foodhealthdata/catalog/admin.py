from django.contrib import admin
from .models import Food, FoodInstance, Nutrient
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(Food)
admin.site.register(FoodInstance)
admin.site.register(Nutrient)

admin.site.register(User)
