# Generated by Django 3.1.2 on 2020-11-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20201110_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
