# Generated by Django 5.0.6 on 2024-06-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccormerceApp', '0003_orderitemmodel_price_orderitemmodel_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(blank=True, choices=[('processing', 'processing'), ('intrasit', 'intrasit'), ('delivered', 'delivered'), ('declined', 'declined')], max_length=255, null=True),
        ),
    ]
