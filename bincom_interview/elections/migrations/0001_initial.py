# Generated by Django 5.1.3 on 2024-11-20 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedPuResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_uniqueid', models.IntegerField()),
                ('party_abbreviation', models.CharField(max_length=10)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=255)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('lga_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('state_id', models.IntegerField()),
                ('polling_unit_name', models.CharField(max_length=255, null=True)),
                ('polling_unit_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=255)),
            ],
        ),
    ]
