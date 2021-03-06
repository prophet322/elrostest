# Generated by Django 3.0.4 on 2020-03-11 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedis', '0005_delete_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordercode', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Тестовое испытание падавана',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedis.Tests')),
            ],
            options={
                'verbose_name_plural': 'Cписок вопросов',
            },
        ),
    ]
