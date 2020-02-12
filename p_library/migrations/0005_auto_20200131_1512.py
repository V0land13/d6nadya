# Generated by Django 2.2.6 on 2020-01-31 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200120_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Reader'),
        ),
    ]
