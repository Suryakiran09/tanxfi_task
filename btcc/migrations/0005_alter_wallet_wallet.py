# Generated by Django 4.2.7 on 2024-04-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btcc', '0004_alter_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet',
            field=models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('DOGE', 'DOGE')], max_length=10),
        ),
    ]
