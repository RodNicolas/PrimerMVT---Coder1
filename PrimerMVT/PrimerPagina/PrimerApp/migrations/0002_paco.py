# Generated by Django 4.1 on 2022-08-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]