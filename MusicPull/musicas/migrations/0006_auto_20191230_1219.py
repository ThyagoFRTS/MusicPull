# Generated by Django 2.2.5 on 2019-12-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0005_clientes_sobrenome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, verbose_name='Usuário')),
                ('password', models.CharField(max_length=40, verbose_name='Senha')),
            ],
            options={
                'verbose_name_plural': 'Logins',
            },
        ),
        migrations.AddField(
            model_name='clientes',
            name='password',
            field=models.CharField(default='password', max_length=40, verbose_name='Senha'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='username',
            field=models.CharField(default='username', max_length=40, verbose_name='Usuário'),
        ),
    ]
