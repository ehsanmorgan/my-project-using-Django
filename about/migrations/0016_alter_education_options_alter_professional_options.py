# Generated by Django 4.1.4 on 2023-01-16 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_alter_skils_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-year',)},
        ),
        migrations.AlterModelOptions(
            name='professional',
            options={'ordering': ('-year',)},
        ),
    ]
