# Generated by Django 4.0.4 on 2022-04-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0002_alter_service_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
