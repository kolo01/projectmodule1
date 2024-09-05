# Generated by Django 5.1.1 on 2024-09-05 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='dishes',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu_dishes', to='dishes.dishesmodel'),
        ),
    ]
