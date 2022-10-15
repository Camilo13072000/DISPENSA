# Generated by Django 4.1.2 on 2022-10-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db_dispensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_fam_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_datos_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_precio', models.IntegerField()),
                ('dat_caducidad', models.DateField()),
                ('dat_gasto', models.IntegerField()),
                ('dat_pro_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_usu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_nombre', models.CharField(max_length=20)),
                ('pro_cantidad', models.IntegerField()),
                ('pro_dis_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usu_nombre', models.CharField(max_length=30)),
                ('usu_password', models.CharField(max_length=40)),
                ('usu_rol', models.CharField(max_length=10)),
            ],
        ),
    ]
