# Generated by Django 3.2.13 on 2023-01-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='lkjlkjlkjlkjlkj', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='6776546546', max_length=50),
            preserve_default=False,
        ),
    ]
