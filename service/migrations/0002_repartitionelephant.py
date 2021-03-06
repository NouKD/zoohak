# Generated by Django 3.1.1 on 2020-11-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepartitionElephant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('population_estimee', models.CharField(blank=True, default='Inconnu', max_length=255, null=True)),
                ('annee', models.DateField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Répartition Elephant',
                'verbose_name_plural': 'Répartitions Elephants',
            },
        ),
    ]
