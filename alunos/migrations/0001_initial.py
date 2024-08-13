# Generated by Django 5.1 on 2024-08-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=12)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
