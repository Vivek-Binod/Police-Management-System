# Generated by Django 5.1.2 on 2024-10-31 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0005_alter_suspect_gender_alter_victim_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspect',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='police.policemodel'),
        ),
        migrations.AddField(
            model_name='victim',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='police.policemodel'),
        ),
    ]
