# Generated by Django 4.1.7 on 2023-05-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappvoiture', '0007_alter_client1_hourformat_alter_client1_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation1',
            name='dateA',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation1',
            name='dateB',
            field=models.DateField(null=True),
        ),
    ]
