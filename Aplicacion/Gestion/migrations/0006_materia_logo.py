# Generated by Django 5.2 on 2025-05-31 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0005_profesor_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='cargos'),
        ),
    ]
