# Generated by Django 3.2.4 on 2021-10-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_gen', '0002_code_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_data',
            name='image',
            field=models.FileField(null=True, upload_to='code_gen/images', verbose_name=''),
        ),
    ]
