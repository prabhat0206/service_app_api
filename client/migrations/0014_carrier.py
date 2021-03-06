# Generated by Django 4.0.4 on 2022-05-19 06:24

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0010_query'),
        ('client', '0013_alter_midorder_service_alter_order_delivery_boy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ph_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('pin_code', models.IntegerField()),
                ('occupation', models.CharField(max_length=255)),
                ('annual_income', models.IntegerField()),
                ('pan_number', models.CharField(max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminn.category')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminn.subcategory')),
            ],
        ),
    ]
