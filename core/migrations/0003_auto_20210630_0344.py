# Generated by Django 3.2.3 on 2021-06-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='controversias',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Controversia'),
        ),
        migrations.AddField(
            model_name='series',
            name='desarrollo',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Desarrollo'),
        ),
        migrations.AddField(
            model_name='series',
            name='sinopsis',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Sinopsis'),
        ),
        migrations.DeleteModel(
            name='Descripcion',
        ),
    ]
