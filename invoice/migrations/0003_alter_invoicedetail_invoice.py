# Generated by Django 4.1 on 2022-08-29 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_remove_invoice_invoice_detail_invoicedetail_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice'),
            preserve_default=False,
        ),
    ]
