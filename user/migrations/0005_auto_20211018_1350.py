# Generated by Django 2.0 on 2021-10-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211018_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Acc_created',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='emailid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='friendslist',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobilenumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
