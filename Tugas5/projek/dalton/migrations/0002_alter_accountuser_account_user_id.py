# Generated by Django 4.2.13 on 2024-07-01 03:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dalton', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('0abb3787-5ac8-4187-92db-05f3f178ae94'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
