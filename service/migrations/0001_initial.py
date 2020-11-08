# Generated by Django 3.1.1 on 2020-11-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(default=1)),
                ('lien_flux', models.TextField(blank=True, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Camera',
                'verbose_name_plural': 'Cameras',
            },
        ),
        migrations.CreateModel(
            name='EspeceMenace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('1', 'Stable'), ('0', 'Contraignant'), ('-1', 'Critique')], max_length=255)),
                ('population_estimee', models.CharField(blank=True, default='Inconnu', max_length=255, null=True)),
                ('menace', models.CharField(blank=True, max_length=255, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Espèce Menacée',
                'verbose_name_plural': 'Espèces Menacées',
            },
        ),
    ]