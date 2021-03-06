# Generated by Django 3.0.4 on 2020-03-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedis', '0003_auto_20200311_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordercode', models.CharField(max_length=100, unique=True)),
                ('taks', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Тестовое испытание падавана',
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='taks',
            new_name='answers',
        ),
    ]
