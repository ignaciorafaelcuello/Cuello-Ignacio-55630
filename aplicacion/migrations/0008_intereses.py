# Generated by Django 4.2.4 on 2023-09-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_cancion_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intereses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intereses', models.CharField(max_length=100000000)),
            ],
            options={
                'verbose_name': 'Interes',
                'verbose_name_plural': 'Intereses',
            },
        ),
    ]
