# Generated by Django 4.1.4 on 2023-01-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_sumary_phemailone_sumary_city_sumary_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
