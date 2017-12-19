# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


def split_price_to_price_net_and_gross(apps, schema_editor):
    Order = apps.get_model('order', 'Order')
    for order in Order.objects.all():
        order.price_net = order.price
        order.price_gross = order.price
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_auto_20171206_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_net',
            field=django_prices.models.AmountField(verbose_name='total net', max_digits=12, decimal_places=2, currency='USD', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_gross',
            field=django_prices.models.AmountField(verbose_name='total gross', max_digits=12, decimal_places=2, currency='USD', blank=True, null=True),
        ),
        migrations.RunPython(split_price_to_price_net_and_gross),
    ]