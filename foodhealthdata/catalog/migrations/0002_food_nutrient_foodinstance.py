# Generated by Django 4.1.7 on 2023-03-08 17:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('fdc_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('histidine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('isoleucine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('leucine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('lysine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('methionine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('phenylalanine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('threonine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('tryptophan', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('valine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('calcium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('potassium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('selenium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('manganese', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('magnesium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('molybdenum', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('iron', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('zinc', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('copper', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('chromium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('iodine', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('phsophorous', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('sodium', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('folate', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('riboflavin', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminA', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('thiamin', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('pantothenicAcid', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('niacin', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('biotin', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('choline', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminB6', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminB12', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminE', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminK', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('vitaminC', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('servingSize', models.PositiveIntegerField()),
                ('servingSizeUnits', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('name', models.CharField(help_text='enter a nutrient name', max_length=200, primary_key=True, serialize=False)),
                ('nutr_id', models.PositiveIntegerField(help_text='enter a nutrient id number', unique=True)),
                ('rdi_male_19y_50y', models.PositiveIntegerField(blank=True, help_text='recommended daily intake for adult males 19-50years', null=True)),
                ('upperTolerance_male_19y_50y', models.PositiveIntegerField(blank=True, help_text='enter an upper tolerance for this nutrient', null=True)),
                ('unit', models.CharField(help_text='enter the units this nutrient is measured in, e.g grams', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='FoodInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('meal', models.PositiveIntegerField()),
                ('fdc_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.food')),
            ],
        ),
    ]