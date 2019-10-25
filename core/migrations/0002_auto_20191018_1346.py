# Generated by Django 2.2.6 on 2019-10-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='tipo',
            field=models.CharField(blank=True, choices=[('CMC_LUZ', 'CMC_LUZ'), ('CR1_LUZ', 'CR1_LUZ'), ('CR2_LUZ', 'CR2_LUZ'), ('CM_LUZ', 'CM_LUZ'), ('CMC_EST', 'CMC_EST'), ('CR1_EST', 'CR1_EST'), ('CR2_EST', 'CR2_EST'), ('CM_EST', 'CM_EST')], max_length=7, null=True, verbose_name='tipo'),
        ),
    ]