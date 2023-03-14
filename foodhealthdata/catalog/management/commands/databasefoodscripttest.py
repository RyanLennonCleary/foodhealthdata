import pandas as pd
import numpy as np
import os
from catalog.models import Food,User
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle (self,*args,**options):

        def createCombined():
            df_food = pd.read_csv('/Users/Ryan1/foodhealthdata/food.csv', usecols=['fdc_id','description'])
            df_food_nutr = pd.read_csv('/Users/Ryan1/foodhealthdata/food_nutrient.csv',usecols=['fdc_id','nutrient_id','amount'])
            df_nutr = pd.read_csv('/Users/Ryan1/foodhealthdata/nutrient.csv',usecols=['id'])
                
            #print(df_nutr.T)
            #print(combined.columns.tolist())
            #print()
            #print(combined[0])
            #print()
            df_nutr1=df_nutr.T
            df_nutr1.columns=df_nutr1.iloc[0,:].tolist()
            combined = pd.concat([df_food,df_nutr1])

            combined.drop('id',inplace=True)
            combined['fdc_id']=combined['fdc_id'].astype(int)
            combined.set_index('fdc_id',inplace=True)
            #print(combined.loc[167512])
            print(combined.loc[df_food_nutr.iloc[0].loc['fdc_id']][df_food_nutr.iloc[0].loc['nutrient_id']])
            print(df_food_nutr.iloc[0].loc['amount'])
            for i in range(0,len(df_food_nutr.index)):
                combined.loc[df_food_nutr.iloc[i].loc['fdc_id'], df_food_nutr.iloc[i].loc['nutrient_id']] = df_food_nutr.iloc[i].loc['amount']
                    #combined = combined.rename(columns=new_dict[i])
            combined.to_csv('combined.csv')
            #print(combined)
            #print()
            #print(type(int(combined.iloc[0].loc['fdc_id'])))
            #print()
            #print(combined.fdc_id.dtype)

            #for i in range(0,len(df_food_nutr.index)):
                #print(combined[str(int(df_food_nutr.iloc[i].loc['fdc_id']))])
                      #combined.loc[df_food_nutr.iloc[i,'fdc_id'],str(int(df_food_nutr.iloc[i,'nutrient_id']))] = df_food_nutr.iloc[i,'value']
            #print(combined)
            #print(combined[str(int(row['nutrient_id']))])
            #print(combined.index[combined['fdc_id']==row['fdc_id']])
        def modifyCombined():
            combined = pd.read_csv('/Users/Ryan1/foodhealthdata/foodhealthdata/combined.csv',index_col='fdc_id')
            print(combined)

            new_dict = {'description':'name','1221': 'histidine','1212':'isoleucine','1213':'leucine','1214':'lysine','1215':'methionine','1217':'phenylalanine','1211':'threonine','1210':'tryptophan','1219':'valine','1087':'calcium','1092':'potassium','1103':'selenium','1101':'manganese','1090':'magnesium','1102':'molybdenum','1089':'iron','1095':'zinc','1098':'copper','1096':'chromium','1100':'iodine','1091':'phsophorous','1093':'sodium','1177':'folate','1166':'riboflavin','1106':'vitaminA','1165':'thiamin','1170':'pantothenicAcid','1167':'niacin','1176':'biotin','1180':'choline','1175':'vitaminB6','1178':'vitaminB12','1158':'vitaminE','1185':'vitaminK','1162':'vitaminC'}

            for i in combined:
                if i in new_dict:
                    combined = combined.rename(columns={i:new_dict[i]})
                else:
                    combined.drop(columns=i,inplace=True)
            combined['servingSize']=100
            combined['servingSizeUnits']='G'
            combined = combined.astype(object).where(combined.notna(),None)
            print(combined)
            return combined


        def createFoods(combined):
            for index,row in combined.iterrows():
                food=Food.objects.create(fdc_id = index, name=row['name'],histidine=row['histidine'],isoleucine=row['isoleucine'],leucine=row['leucine'],lysine=row['lysine'],methionine=row['methionine'],phenylalanine=row['phenylalanine'],threonine=row['threonine'],tryptophan=row['tryptophan'],valine=row['valine'],calcium=row['calcium'],potassium=row['potassium'],selenium=row['selenium'],manganese=row['manganese'],magnesium=row['magnesium'],molybdenum=row['molybdenum'],iron=row['iron'],zinc=row['zinc'],copper=row['copper'],chromium=row['chromium'],iodine=row['iodine'],phsophorous=row['phsophorous'],sodium=row['sodium'],folate=row['folate'],riboflavin=row['riboflavin'],vitaminA=row['vitaminA'],thiamin=row['thiamin'],pantothenicAcid=row['pantothenicAcid'],niacin=row['niacin'],biotin=row['biotin'],choline=row['choline'],vitaminB6=row['vitaminB6'],vitaminB12=row['vitaminB12'],vitaminE=row['vitaminE'],vitaminK=row['vitaminK'],vitaminC=row['vitaminC'],servingSize=row['servingSize'],servingSizeUnits=row['servingSizeUnits'])
                food.save()
        combined = modifyCombined()
        createFoods(combined)
        print(combined)
