# Generated by Django 3.0.8 on 2020-10-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_doctor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]