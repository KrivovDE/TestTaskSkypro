# Generated by Django 4.2.1 on 2023-05-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.CharField(choices=[('junior', 'Junior'), ('midle', 'Midle'), ('senior', 'Senior')], default='junior', max_length=20),
        ),
    ]