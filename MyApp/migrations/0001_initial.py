# Generated by Django 3.2.1 on 2023-06-01 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('common_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('common_name', models.CharField(max_length=20)),
                ('common_tel', models.CharField(max_length=20)),
                ('common_address', models.CharField(max_length=50)),
                ('common_email', models.CharField(max_length=50)),
                ('common_integral', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=20)),
                ('manager_tel', models.CharField(max_length=20)),
                ('manager_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
                ('type_kind', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20)),
                ('user_identity', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Throw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_id', models.CharField(max_length=20)),
                ('common_tel', models.CharField(max_length=20)),
                ('dump_id', models.CharField(max_length=20)),
                ('dump_place', models.CharField(max_length=20)),
                ('throw_time', models.CharField(max_length=20)),
                ('dump_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.type')),
            ],
        ),
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('dump_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dump_number', models.IntegerField()),
                ('dump_place', models.CharField(max_length=20)),
                ('dump_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.type')),
            ],
        ),
    ]
