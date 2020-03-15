# Generated by Django 3.0.4 on 2020-03-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_auto_20200314_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoneed',
            name='resolved_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Resolved on'),
        ),
        migrations.AddField(
            model_name='ngoneed',
            name='title',
            field=models.CharField(default='Avem nevoie de 1000 de baxuri de apa', max_length=254, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
