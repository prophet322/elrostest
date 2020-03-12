# Generated by Django 3.0.4 on 2020-03-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedis', '0006_questions_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='text',
            field=models.TextField(verbose_name='Суть вопроса'),
        ),
        migrations.AlterField(
            model_name='tests',
            name='ordercode',
            field=models.CharField(max_length=100, unique=True, verbose_name='Код ордена'),
        ),
    ]