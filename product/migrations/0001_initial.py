# Generated by Django 3.0.8 on 2020-07-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Marque du produit')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Nom de la catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Nom du magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField(unique=True, verbose_name='Code barre')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du produit')),
                ('common_name', models.CharField(blank=True, max_length=100, verbose_name='Nom générique')),
                ('quantity', models.CharField(blank=True, max_length=50, verbose_name='Quantité')),
                ('ingredients_text', models.TextField(blank=True, verbose_name='Ingrédients')),
                ('nutriscore_grade', models.CharField(max_length=1, verbose_name='Nutriscore')),
                ('url', models.CharField(max_length=250, verbose_name='Url du produit')),
                ('brands', models.ManyToManyField(to='product.Brand')),
                ('categories', models.ManyToManyField(to='product.Category')),
                ('stores', models.ManyToManyField(to='product.Store')),
            ],
        ),
    ]