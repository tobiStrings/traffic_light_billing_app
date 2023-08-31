# Generated by Django 4.2.4 on 2023-08-30 21:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('traffic_light', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=19)),
                ('payment_code', models.CharField(max_length=6)),
                ('number_plate', models.CharField(max_length=8)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('traffic_light', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='traffic_light.trafficlight')),
            ],
        ),
    ]