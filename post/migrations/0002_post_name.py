# Generated by Django 4.1.4 on 2023-02-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
