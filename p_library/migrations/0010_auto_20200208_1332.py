# Generated by Django 2.2.6 on 2020-02-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_auto_20200208_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, help_text='20x20px', upload_to=''),
        ),
    ]
