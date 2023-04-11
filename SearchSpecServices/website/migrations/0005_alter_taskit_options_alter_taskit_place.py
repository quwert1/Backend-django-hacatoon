# Generated by Django 4.2 on 2023-04-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_taskit_options_taskit_time_create_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskit',
            options={'ordering': ['-time_update', 'title'], 'verbose_name': 'Списки заказов от заказчиков', 'verbose_name_plural': 'Списки заказов от заказчиков'},
        ),
        migrations.AlterField(
            model_name='taskit',
            name='place',
            field=models.CharField(max_length=255),
        ),
    ]