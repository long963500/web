# Generated by Django 2.2.4 on 2020-04-17 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0054_auto_20200414_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='amount_goal',
        ),
    ]
