# Generated by Django 3.0.3 on 2020-02-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietmanager', '0005_healthmodel_diseases'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storagemodel',
            old_name='to_eat',
            new_name='daily_intake1',
        ),
        migrations.RemoveField(
            model_name='storagemodel',
            name='diet',
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='daily_intake7',
            field=models.IntegerField(default=0),
        ),
    ]
