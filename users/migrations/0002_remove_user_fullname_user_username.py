# Generated by Django 4.1 on 2022-08-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
