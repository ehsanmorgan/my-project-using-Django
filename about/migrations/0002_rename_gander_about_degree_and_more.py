# Generated by Django 4.1.4 on 2023-01-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='gander',
            new_name='Degree',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='lives_in',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='about',
            name='from_adresse',
        ),
        migrations.AddField(
            model_name='about',
            name='PhEmailone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='Website',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='brithday',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='freelance',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
