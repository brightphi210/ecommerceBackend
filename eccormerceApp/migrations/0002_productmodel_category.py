# Generated by Django 5.0.6 on 2024-06-06 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccormerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eccormerceApp.categorymodel'),
        ),
    ]
