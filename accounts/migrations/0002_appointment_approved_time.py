# Generated by Django 3.0.8 on 2020-11-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='approved_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
