# Generated by Django 4.0.2 on 2022-04-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolsManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maxSpeed',
            field=models.FloatField(blank=True, null=True, verbose_name='Max Speed'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workspaceLimitX',
            field=models.FloatField(blank=True, null=True, verbose_name='Workspace Limit X'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workspaceLimitY',
            field=models.FloatField(blank=True, null=True, verbose_name='Workspace Limit Y'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workspaceLimitZ',
            field=models.FloatField(blank=True, null=True, verbose_name='Workspace Limit Z'),
        ),
    ]