# Generated by Django 4.0.6 on 2022-08-11 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0015_team_remove_user_user_name_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Account.team'),
        ),
    ]