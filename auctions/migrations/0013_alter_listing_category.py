# Generated by Django 3.2.7 on 2022-02-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_data_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Asian', 'Asian'), ('European', 'European'), ('GlutenFree', 'Gluten Free'), ('Low Fat', 'Low Fat'), ('Keto', 'Keto'), ('Others', 'Others')], default='Others', max_length=1000),
        ),
    ]