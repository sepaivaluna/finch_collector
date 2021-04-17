# Generated by Django 3.2 on 2021-04-17 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('country_of_residency', models.CharField(max_length=20)),
                ('supports', models.CharField(choices=[('A', 'Team A'), ('B', 'Team B')], default='A', max_length=1)),
                ('world_cup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.world_cup')),
            ],
        ),
    ]
