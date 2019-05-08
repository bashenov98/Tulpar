# Generated by Django 2.2.1 on 2019-05-08 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employees', to='user.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='user.Company'),
        ),
    ]
