# Generated by Django 4.1.1 on 2024-05-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmaster_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='updated_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='updated_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productupdatehistory',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productupdatehistory',
            name='updated_at',
            field=models.CharField(max_length=255),
        ),
    ]
