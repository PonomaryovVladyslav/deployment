# Generated by Django 3.1.2 on 2020-11-10 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20201106_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='myapp.item'),
        ),
    ]
