# Generated by Django 2.1.4 on 2019-01-01 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviealert', '0002_cinemas_subregion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviealert.Region'),
        ),
    ]
