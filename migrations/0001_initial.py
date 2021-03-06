# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 20:34
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id_agenda', models.AutoField(primary_key=True, serialize=False)),
                ('dtfecha_cita', models.DateTimeField(null=True, verbose_name='Fecha cita')),
                ('dtfecha_fin_cita', models.DateTimeField(blank=True, null=True, verbose_name='Fecha fin cita')),
                ('dtfecha_reprogramada', models.DateTimeField(blank=True, null=True, verbose_name='Reprogramacion')),
                ('cObservaciones', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observaciones')),
                ('cEstatus', models.CharField(choices=[('P', 'Programada'), ('C', 'En Curso'), ('F', 'Finalizada')], max_length=15, null=True, verbose_name='Estatus')),
                ('itelefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Celular')),
                ('ifijo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Teléfono fijo')),
                ('iext', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Extencion')),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Agendados',
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id_clinica', models.AutoField(primary_key=True, serialize=False)),
                ('cclinica', models.CharField(max_length=100, null=True, verbose_name='Clínica')),
                ('cdescripcion', models.CharField(max_length=200, null=True, verbose_name='Descripcion')),
                ('ccalle', models.CharField(max_length=200, null=True, verbose_name='Calle')),
                ('cnum_int', models.CharField(max_length=10, null=True, verbose_name='Interior')),
                ('cnum_ext', models.CharField(max_length=10, null=True, verbose_name='Exterior')),
                ('ccp', models.CharField(max_length=10, null=True, verbose_name='Codigo postal')),
                ('id_ubicacion', models.IntegerField()),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id_consulta', models.AutoField(primary_key=True, serialize=False)),
                ('dtfecha_consulta', models.DateTimeField(verbose_name='Fecha consulta')),
                ('dtfecha_fin_consulta', models.DateTimeField(verbose_name='Fecha fin consulta')),
                ('cestatus', models.CharField(blank=True, choices=[('P', 'Programada'), ('C', 'En Curso'), ('F', 'Finalizada')], max_length=10, null=True, verbose_name='Estatus')),
                ('dHonorarios', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, null=True, verbose_name='honorarios')),
                ('cObservaciones', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observaciones')),
                ('cSintomatologia', models.CharField(max_length=1000, null=True, verbose_name='Sintomatología')),
                ('cDiagnostico', models.CharField(max_length=1000, null=True, verbose_name='Diagnostico')),
                ('dtalla', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Talla')),
                ('dpeso', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Peso')),
                ('iedad', models.IntegerField(null=True, verbose_name='Edad')),
                ('imeses', models.IntegerField(null=True, verbose_name='Meses')),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
                ('id_cita', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Agenda')),
            ],
            options={
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id_consultorio', models.AutoField(primary_key=True, serialize=False)),
                ('id_clinica', models.IntegerField()),
                ('cnumero_consultorio', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero de consultorio')),
                ('cdescripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Referencia')),
                ('cubicacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('cdias_atencion', models.CharField(max_length=200, null=True, verbose_name='Dias de atención')),
                ('chorario_ini', models.CharField(max_length=200, null=True, verbose_name='Horario inicio')),
                ('chorario_fin', models.CharField(max_length=200, null=True, verbose_name='Horario fin')),
                ('iintervalo_consulta', models.IntegerField(default=1, null=True)),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Consultorios',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('cespecialidad', models.CharField(max_length=50, null=True, verbose_name='Especialidad')),
                ('cdescripcion', models.CharField(max_length=200, null=True, verbose_name='Descripcion')),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccedula_profesional', models.CharField(max_length=50, null=True, verbose_name='Cédula profesional')),
                ('ccedula_especialidad', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cédula especialidad')),
                ('dtfecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('cgenero', models.CharField(choices=[('M', 'Hombre'), ('F', 'Mujer')], default='M', max_length=2, verbose_name='Genero')),
                ('id_direccion', models.IntegerField()),
                ('ccorreo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('itelefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Celular')),
                ('ifijo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Teléfono fijo')),
                ('iext', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Extencion')),
                ('cdatos_curriculares', models.CharField(blank=True, max_length=500, null=True, verbose_name='Datos curriculares')),
                ('cespecialidades', models.CharField(blank=True, max_length=500, null=True, verbose_name='Especialidades')),
                ('cfacebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook')),
                ('ctwiter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Twiter')),
                ('csitio_web', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sitio Web')),
                ('ccalle', models.CharField(max_length=200, null=True, verbose_name='Calle')),
                ('cnum_int', models.CharField(max_length=10, null=True, verbose_name='Interior')),
                ('cnum_ext', models.CharField(max_length=10, null=True, verbose_name='Exterior')),
                ('ccp', models.CharField(max_length=10, null=True, verbose_name='Codigo postal')),
                ('id_ubicacion', models.IntegerField()),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
                ('id_especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicadmin.Especialidad')),
            ],
            options={
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('cnombre', models.CharField(max_length=50, null=True, verbose_name='Nombre')),
                ('cpaterno', models.CharField(max_length=50, null=True, verbose_name='Apellido paterno')),
                ('cmaterno', models.CharField(max_length=50, null=True, verbose_name='Apellido materno')),
                ('dtfecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('cgenero', models.CharField(choices=[('M', 'Hombre'), ('F', 'Mujer')], default='M', max_length=2, verbose_name='Genero')),
                ('ccorreo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('itelefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Celular')),
                ('ifijo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Teléfono fijo')),
                ('iext', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Extencion')),
                ('calergias', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alergias')),
                ('cenfermedades_cronicas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cronicas')),
                ('ccalle', models.CharField(max_length=200, null=True, verbose_name='Calle')),
                ('cnum_int', models.CharField(max_length=10, null=True, verbose_name='Interior')),
                ('cnum_ext', models.CharField(max_length=10, null=True, verbose_name='Exterior')),
                ('ccp', models.CharField(max_length=10, null=True, verbose_name='Codigo postal')),
                ('id_ubicacion', models.IntegerField()),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id_receta', models.AutoField(primary_key=True, serialize=False)),
                ('iorden_medicamento', models.IntegerField(verbose_name='Orden')),
                ('cmedicamento', models.CharField(max_length=200, null=True, verbose_name='Medicamento')),
                ('cfrecuencia', models.CharField(max_length=200, null=True, verbose_name='Frecuencia de toma')),
                ('cperiodo', models.CharField(max_length=200, null=True, verbose_name='Periodo de toma')),
                ('cindicaciones', models.CharField(blank=True, max_length=200, null=True, verbose_name='Indicaciones')),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
                ('id_constulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Consulta')),
            ],
            options={
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id_universidad', models.AutoField(primary_key=True, serialize=False)),
                ('cuniversidad', models.CharField(max_length=50, null=True, verbose_name='Universidad')),
                ('cdescripcion', models.CharField(max_length=200, null=True, verbose_name='Descripcion')),
                ('dtcreacion', models.DateTimeField(auto_now=True, verbose_name='Creación')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Universidades',
            },
        ),
        migrations.AddField(
            model_name='medico',
            name='id_univeridad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicadmin.Universidad'),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='id_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_consultorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Consultorio'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Paciente'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='id_consultorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Consultorio'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicadmin.Paciente'),
        ),
    ]
