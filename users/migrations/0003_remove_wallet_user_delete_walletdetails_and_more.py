# Generated by Django 4.2.7 on 2024-04-08 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_walletdetails_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.DeleteModel(
            name='WalletDetails',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
