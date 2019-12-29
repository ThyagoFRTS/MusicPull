# Generated by Django 2.2.5 on 2019-12-29 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0002_auto_20191028_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.AlterField(
            model_name='albuns',
            name='ano',
            field=models.IntegerField(verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='albuns',
            name='duracao',
            field=models.DurationField(verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='albuns',
            name='num_musicas',
            field=models.IntegerField(verbose_name='Número de Músicas'),
        ),
        migrations.AlterField(
            model_name='albuns',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='albuns',
            name='titulo',
            field=models.CharField(max_length=40, verbose_name='Título'),
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicas.Albuns')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicas.Clientes')),
            ],
            options={
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
