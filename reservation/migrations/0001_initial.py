# Generated by Django 3.0.4 on 2020-03-31 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('sits', models.PositiveIntegerField(default=2)),
                ('shape', models.IntegerField(choices=[(1, 'Rectangle'), (2, 'Ellipse')])),
                ('coordinateX', models.IntegerField()),
                ('coordinateY', models.IntegerField()),
                ('length', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='reservation.Table')),
            ],
        ),
    ]