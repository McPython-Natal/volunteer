# Generated by Django 3.0.5 on 2020-12-10 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vol', '0003_pandemic'),
    ]

    operations = [
        migrations.AddField(
            model_name='pandemic',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('pandemic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vol.Pandemic')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vol.Volunteer')),
            ],
        ),
    ]
