# Generated by Django 2.0 on 2021-10-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211018_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Acc_created',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='friendslist',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
