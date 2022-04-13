# Generated by Django 4.0.3 on 2022-04-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studiengang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fachbereich', models.CharField(choices=[('EI', 'Elektrotechnik und Informatik'), ('G', 'Geodäsie')], max_length=200)),
                ('abschulss', models.CharField(choices=[('BA', 'Bachelor'), ('MA', 'Master')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pruefung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updateTime', models.DateTimeField(auto_created=True)),
                ('createTime', models.DateTimeField(auto_created=True)),
                ('pnr', models.IntegerField(unique=True)),
                ('semester', models.IntegerField()),
                ('name', models.CharField(max_length=200, unique=True)),
                ('pruefer', models.CharField(max_length=200)),
                ('datum', models.DateField()),
                ('pruefungsform', models.CharField(max_length=200)),
                ('dauer', models.IntegerField()),
                ('teilnehmerzahl', models.IntegerField()),
                ('pruefungsOrdnung', models.IntegerField()),
                ('fachbereich', models.ManyToManyField(to='api.studiengang')),
            ],
        ),
    ]