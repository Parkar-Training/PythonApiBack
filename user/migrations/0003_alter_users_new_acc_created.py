# Generated by Django 3.2 on 2021-10-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_users_new_acc_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_new',
            name='acc_created',
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
    ]