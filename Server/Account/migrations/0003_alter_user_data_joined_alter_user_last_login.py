# Generated by Django 4.0.6 on 2022-08-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Last login'),
        ),
    ]