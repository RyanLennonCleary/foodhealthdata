# Generated by Django 4.1.7 on 2023-03-13 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_food_vitaminb6_food_vitaminb9_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='vitaminB9',
            new_name='vitaminB6',
        ),
    ]
