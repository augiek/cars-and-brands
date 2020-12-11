# Generated by Django 3.1.4 on 2020-12-10 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('brand_country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand')),
            ],
        ),
    ]
