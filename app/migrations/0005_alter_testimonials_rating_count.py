# Generated by Django 5.0 on 2025-02-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_testimonials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='rating_count',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
