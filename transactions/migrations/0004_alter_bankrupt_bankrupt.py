# Generated by Django 4.2.7 on 2024-01-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_bankrupt_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankrupt',
            name='bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]
