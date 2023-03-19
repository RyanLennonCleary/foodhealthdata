import uuid
from datetime import datetime,date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from foodhealthdata import settings

# Create your models here.
class Nutrient(models.Model):
    name = models.CharField(max_length=200, help_text='enter a nutrient name',primary_key=True)
    nutr_id = models.PositiveIntegerField(unique=True, help_text='enter a nutrient id number')
    rdi_male = models.PositiveIntegerField(blank=True, null=True,help_text='recommended daily intake for adult males 19-50years')
    rdi_female = models.PositiveIntegerField(blank=True, null=True,help_text='recommended daily intake for adult males 19-50years')
    upperTolerance = models.BooleanField(blank=True, null=True,help_text='enter an upper tolerance for this nutrient')
    unit = models.CharField(max_length=5,help_text='enter the units this nutrient is measured in, e.g grams')
    def __str__(self):
        return self.name

class Food(models.Model):
    fdc_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    histidine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    isoleucine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    leucine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    lysine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    methionine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    phenylalanine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    threonine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    tryptophan = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    valine = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    calcium = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    potassium = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    selenium = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    manganese = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    magnesium = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    molybdenum = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    iron = models.DecimalField(max_digits=9,decimal_places=3,default=0,null=True)
    zinc = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    copper = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    chromium = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    iodine = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    phsophorous = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    sodium = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    folate = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    riboflavin = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    vitaminA = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    thiamin = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    pantothenicAcid = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    niacin = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    biotin = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    choline = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    vitaminB6 = models.DecimalField(max_digits=6, decimal_places=3,default=0,null=True)
    vitaminB12 = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    vitaminE = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    vitaminK = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    vitaminC = models.DecimalField(max_digits=9, decimal_places=3,default=0,null=True)
    servingSize = models.PositiveIntegerField()
    servingSizeUnits = models.CharField(max_length=5)
    def get_fields(self):
        return [(field.name, getattr(self, field.name)) for field in Food._meta.fields]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('food-detail', args=[str(self.fdc_id)])
    def printHello(self):
        return 1

class FoodInstance(models.Model):
    eater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    fdc_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date_eaten = models.DateField(default=date.today)
    meal = models.PositiveIntegerField(default=0)
    class Meta:
        permissions = (("can_remove_foodinstance", "remove food"),)

    def __str__(self):
        return f'{self.id} ({self.fdc_id.name})'

class User(AbstractUser):
    pass
