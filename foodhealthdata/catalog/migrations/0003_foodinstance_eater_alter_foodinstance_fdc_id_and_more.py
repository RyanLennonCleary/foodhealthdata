# Generated by Django 4.1.7 on 2023-03-10 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_food_nutrient_foodinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodinstance',
            name='eater',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodinstance',
            name='fdc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.food'),
        ),
        migrations.AlterField(
            model_name='foodinstance',
            name='meal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
