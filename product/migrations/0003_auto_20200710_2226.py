# Generated by Django 3.0.8 on 2020-07-10 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200710_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.MinLengthValidator(13), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutriscore_grade',
            field=models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator, django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator]),
        ),
    ]