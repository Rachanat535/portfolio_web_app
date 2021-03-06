# Generated by Django 3.1.4 on 2021-01-31 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_expertise'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expertise',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='expertise',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
