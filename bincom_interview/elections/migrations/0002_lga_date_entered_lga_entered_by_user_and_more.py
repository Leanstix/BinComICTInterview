# Generated by Django 5.1.3 on 2024-11-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(default='2000-01-01 00:00:00'),
        ),
        migrations.AddField(
            model_name='lga',
            name='entered_by_user',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AddField(
            model_name='lga',
            name='lga_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lga',
            name='user_ip_address',
            field=models.CharField(default='127.0.0.1', max_length=50),
        ),
        migrations.AlterField(
            model_name='lga',
            name='lga_name',
            field=models.CharField(max_length=50),
        ),
    ]
