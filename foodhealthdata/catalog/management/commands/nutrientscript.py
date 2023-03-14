import as pd
from catalog.models import Nutrient
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle (self,*args,**options):
        df_nutrients = pd.read_csv('/Users/Ryan1/foodhealthdata/nihnutrients.csv',index_col='name')


