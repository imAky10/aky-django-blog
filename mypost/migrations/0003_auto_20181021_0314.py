# Generated by Django 2.1.2 on 2018-10-20 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0002_auto_20181020_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='blog_content',
        ),
    ]
