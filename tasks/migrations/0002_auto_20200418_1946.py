# Generated by Django 3.0.4 on 2020-04-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
