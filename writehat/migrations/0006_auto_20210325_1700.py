# Generated by Django 3.1.7 on 2021-03-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writehat', '0005_auto_20210325_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asvsengagementfinding',
            name='asvsStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
