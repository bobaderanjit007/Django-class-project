# Generated by Django 4.2.7 on 2024-01-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to='productImages/'),
        ),
    ]