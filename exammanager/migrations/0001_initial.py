# Generated by Django 2.2.3 on 2019-09-16 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=50)),
                ('block', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('department', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Allocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatno', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exammanager.AddHall')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exammanager.AddStudent')),
            ],
        ),
    ]
