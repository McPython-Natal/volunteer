# Generated by Django 3.0.5 on 2020-12-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vol', '0006_auto_20201210_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]