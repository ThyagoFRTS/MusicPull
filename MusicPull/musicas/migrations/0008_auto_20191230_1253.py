# Generated by Django 2.2.5 on 2019-12-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0007_auto_20191230_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='login',
        ),
        migrations.AddField(
            model_name='logins',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicas.Clientes'),
        ),
    ]
