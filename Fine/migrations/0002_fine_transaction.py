# Generated by Django 3.0.2 on 2020-10-16 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Transactions', '0001_initial'),
        ('Fine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Transactions.Transaction'),
        ),
    ]
