# Generated by Django 5.0.6 on 2024-06-20 12:50

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oficina', models.CharField(choices=[('Administrativo', 'Administrativo'), ('Formacion', 'Formacion')], max_length=15)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProcedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.TextField(default='sin descripcion', max_length=2000)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('tipoUsuario', models.CharField(choices=[('Administrador', 'Administrador'), ('Instructor', 'Instructor')], max_length=50)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appService.oficina')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('estado', models.CharField(choices=[('Solicitada', 'Solicitada'), ('En Proceso', 'En Proceso'), ('Finalizada', 'Finalizada')], default='Solicitada', max_length=20)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
                ('casoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appService.solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionCaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedimiento', models.TextField(max_length=2000)),
                ('tipoSolucion', models.CharField(choices=[('Parcial', 'Parcial'), ('Definitiva', 'Definitiva')], max_length=20)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True)),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appService.caso')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionCasoTipoProcedimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solucionCaso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appService.solucioncaso')),
                ('tipoProcedimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appService.tipoprocedimiento')),
            ],
        ),
    ]
