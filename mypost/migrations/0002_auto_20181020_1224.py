# Generated by Django 2.1.2 on 2018-10-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]