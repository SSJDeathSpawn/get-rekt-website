# Generated by Django 4.2 on 2023-04-14 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=20)),
                ('max', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.IntegerField()),
                ('discordid', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['regno'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamreg.game')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]