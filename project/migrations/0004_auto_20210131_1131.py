# Generated by Django 3.1.4 on 2021-01-31 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20201228_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created_at',), 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='projectcategory',
            options={'verbose_name': 'Project Category', 'verbose_name_plural': 'Project Categories'},
        ),
    ]
