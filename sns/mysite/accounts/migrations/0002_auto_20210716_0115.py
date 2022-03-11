# Generated by Django 3.2.5 on 2021-07-15 16:15

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='icond_name',
            new_name='icon',
        ),
    ]
