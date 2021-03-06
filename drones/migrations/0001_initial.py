# Generated by Django 3.1.2 on 2020-10-27 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=150)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=2)),
                ('quant_corridas', models.IntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('data', models.DateTimeField()),
                ('competindo', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('drone_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drone', to='drones.dronecategoria')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura_em_pes', models.IntegerField()),
                ('distancia_na_data', models.DateTimeField()),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competicoes', to='drones.piloto')),
            ],
            options={
                'ordering': ('-altura_em_pes',),
            },
        ),
    ]
