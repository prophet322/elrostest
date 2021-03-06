# Generated by Django 3.0.4 on 2020-03-11 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Список планет',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordercode', models.CharField(max_length=100, unique=True)),
                ('text', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Список вопросов',
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedis.Planet')),
            ],
            options={
                'verbose_name_plural': 'Список Джидаев',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('taks', models.TextField(blank=True)),
                ('jedi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedis.Jedi')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedis.Planet')),
            ],
        ),
    ]
