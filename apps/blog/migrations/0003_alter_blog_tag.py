# Generated by Django 3.2.16 on 2022-10-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_how_it_works_hiw_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]