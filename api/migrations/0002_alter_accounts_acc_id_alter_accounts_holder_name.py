# Generated by Django 4.2.1 on 2023-05-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='acc_id',
            field=models.BigIntegerField(default=202305040001),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='holder_name',
            field=models.TextField(max_length=50),
        ),
    ]
