# Generated by Django 3.2.13 on 2023-02-04 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('orders', models.IntegerField(default=0)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
