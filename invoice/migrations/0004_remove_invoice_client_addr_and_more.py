# Generated by Django 4.1 on 2022-08-29 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('invoice', '0003_alter_invoicedetail_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='client_addr',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='client_name',
        ),
        migrations.AddField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
