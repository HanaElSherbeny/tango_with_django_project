# Generated by Django 2.2.26 on 2022-01-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_delete_pageadmin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]