# Generated by Django 4.1.1 on 2022-09-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_bookinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('0', 'Maintenance'), ('1', 'On loan'), ('2', 'Available'), ('3', 'Reserved')], help_text='Status of the Instance.', max_length=1),
        ),
    ]
