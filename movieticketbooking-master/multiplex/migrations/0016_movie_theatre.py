# Generated by Django 3.0.5 on 2020-10-14 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0015_tempmovie_theatre_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='theatre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='multiplex.Theatre'),
        ),
    ]
