# Generated by Django 4.1.1 on 2022-09-07 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='instanceId',
            new_name='id',
        ),
    ]
