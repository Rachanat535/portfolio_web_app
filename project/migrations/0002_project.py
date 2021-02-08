# Generated by Django 3.0.4 on 2020-12-28 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_file', models.ImageField(null=True, upload_to='pictures/')),
                ('owner', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('is_popular', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectCategory')),
            ],
        ),
    ]
