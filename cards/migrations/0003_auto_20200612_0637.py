# Generated by Django 3.0.7 on 2020-06-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20200612_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='is_reported',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
