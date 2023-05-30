# Generated by Django 4.1.7 on 2023-05-24 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('revenue', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('nationality', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('age', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('carType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.cartype')),
            ],
        ),
    ]