# Generated by Django 4.1.4 on 2023-01-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_alter_about_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='skils',
            name='subtitle',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skils',
            name='title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
