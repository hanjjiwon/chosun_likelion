# Generated by Django 3.0.3 on 2020-02-23 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_code',
            fields=[
                ('subject_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_range',
            fields=[
                ('subject_range', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Write_index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('attendance', models.CharField(max_length=20)),
                ('test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50, null=True)),
                ('professor', models.CharField(max_length=50)),
                ('recommendation', models.IntegerField(default=0)),
                ('nonrecommendation', models.IntegerField(default=0)),
                ('homework_large', models.IntegerField(default=0)),
                ('homework_medium', models.IntegerField(default=0)),
                ('homework_small', models.IntegerField(default=0)),
                ('homework_best', models.CharField(max_length=20, null=True)),
                ('team_yes', models.IntegerField(default=0)),
                ('team_no', models.IntegerField(default=0)),
                ('team_best', models.CharField(max_length=20, null=True)),
                ('grade_good', models.IntegerField(default=0)),
                ('grade_bad', models.IntegerField(default=0)),
                ('grade_f', models.IntegerField(default=0)),
                ('grade_best', models.CharField(max_length=20, null=True)),
                ('attendance_speak', models.IntegerField(default=0)),
                ('attendance_elec', models.IntegerField(default=0)),
                ('attendance_none', models.IntegerField(default=0)),
                ('attendance_best', models.CharField(max_length=20, null=True)),
                ('test_3', models.IntegerField(default=0)),
                ('test_2', models.IntegerField(default=0)),
                ('test_1', models.IntegerField(default=0)),
                ('test_0', models.IntegerField(default=0)),
                ('test_best', models.CharField(max_length=20, null=True)),
                ('subject_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='write.Subject_range')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_id', models.CharField(max_length=20)),
                ('evaluation_text', models.TextField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='write.Subject')),
            ],
        ),
    ]
