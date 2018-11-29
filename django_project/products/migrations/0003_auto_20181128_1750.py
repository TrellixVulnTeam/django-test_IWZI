# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-28 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181128_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categ_name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_categ_name',
            new_name='sub_category_name',
        ),
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.SubCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
            preserve_default=False,
        ),
    ]