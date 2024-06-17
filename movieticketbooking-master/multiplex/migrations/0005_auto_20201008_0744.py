# Generated by Django 3.0.5 on 2020-10-08 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0004_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie_pic/movie_poster/'),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('a1', models.BooleanField(default=True)),
                ('a2', models.BooleanField(default=True)),
                ('a3', models.BooleanField(default=True)),
                ('a4', models.BooleanField(default=True)),
                ('a5', models.BooleanField(default=True)),
                ('a6', models.BooleanField(default=True)),
                ('a7', models.BooleanField(default=True)),
                ('a8', models.BooleanField(default=True)),
                ('a9', models.BooleanField(default=True)),
                ('a10', models.BooleanField(default=True)),
                ('a11', models.BooleanField(default=True)),
                ('a12', models.BooleanField(default=True)),
                ('b1', models.BooleanField(default=True)),
                ('b2', models.BooleanField(default=True)),
                ('b3', models.BooleanField(default=True)),
                ('b4', models.BooleanField(default=True)),
                ('b5', models.BooleanField(default=True)),
                ('b6', models.BooleanField(default=True)),
                ('b7', models.BooleanField(default=True)),
                ('b8', models.BooleanField(default=True)),
                ('b9', models.BooleanField(default=True)),
                ('b10', models.BooleanField(default=True)),
                ('b11', models.BooleanField(default=True)),
                ('b12', models.BooleanField(default=True)),
                ('c1', models.BooleanField(default=True)),
                ('c2', models.BooleanField(default=True)),
                ('c3', models.BooleanField(default=True)),
                ('c4', models.BooleanField(default=True)),
                ('c5', models.BooleanField(default=True)),
                ('c6', models.BooleanField(default=True)),
                ('c7', models.BooleanField(default=True)),
                ('c8', models.BooleanField(default=True)),
                ('c9', models.BooleanField(default=True)),
                ('c10', models.BooleanField(default=True)),
                ('c11', models.BooleanField(default=True)),
                ('c12', models.BooleanField(default=True)),
                ('d1', models.BooleanField(default=True)),
                ('d2', models.BooleanField(default=True)),
                ('d3', models.BooleanField(default=True)),
                ('d4', models.BooleanField(default=True)),
                ('d5', models.BooleanField(default=True)),
                ('d6', models.BooleanField(default=True)),
                ('d7', models.BooleanField(default=True)),
                ('d8', models.BooleanField(default=True)),
                ('d9', models.BooleanField(default=True)),
                ('d10', models.BooleanField(default=True)),
                ('d11', models.BooleanField(default=True)),
                ('d12', models.BooleanField(default=True)),
                ('e1', models.BooleanField(default=True)),
                ('e2', models.BooleanField(default=True)),
                ('e3', models.BooleanField(default=True)),
                ('e4', models.BooleanField(default=True)),
                ('e5', models.BooleanField(default=True)),
                ('e6', models.BooleanField(default=True)),
                ('e7', models.BooleanField(default=True)),
                ('e8', models.BooleanField(default=True)),
                ('e9', models.BooleanField(default=True)),
                ('e10', models.BooleanField(default=True)),
                ('e11', models.BooleanField(default=True)),
                ('e12', models.BooleanField(default=True)),
                ('f1', models.BooleanField(default=True)),
                ('f2', models.BooleanField(default=True)),
                ('f3', models.BooleanField(default=True)),
                ('f4', models.BooleanField(default=True)),
                ('f5', models.BooleanField(default=True)),
                ('f6', models.BooleanField(default=True)),
                ('f7', models.BooleanField(default=True)),
                ('f8', models.BooleanField(default=True)),
                ('f9', models.BooleanField(default=True)),
                ('f10', models.BooleanField(default=True)),
                ('f11', models.BooleanField(default=True)),
                ('f12', models.BooleanField(default=True)),
                ('g1', models.BooleanField(default=True)),
                ('g2', models.BooleanField(default=True)),
                ('g3', models.BooleanField(default=True)),
                ('g4', models.BooleanField(default=True)),
                ('g5', models.BooleanField(default=True)),
                ('g6', models.BooleanField(default=True)),
                ('g7', models.BooleanField(default=True)),
                ('g8', models.BooleanField(default=True)),
                ('g9', models.BooleanField(default=True)),
                ('g10', models.BooleanField(default=True)),
                ('g11', models.BooleanField(default=True)),
                ('g12', models.BooleanField(default=True)),
                ('h1', models.BooleanField(default=True)),
                ('h2', models.BooleanField(default=True)),
                ('h3', models.BooleanField(default=True)),
                ('h4', models.BooleanField(default=True)),
                ('h5', models.BooleanField(default=True)),
                ('h6', models.BooleanField(default=True)),
                ('h7', models.BooleanField(default=True)),
                ('h8', models.BooleanField(default=True)),
                ('h9', models.BooleanField(default=True)),
                ('h10', models.BooleanField(default=True)),
                ('h11', models.BooleanField(default=True)),
                ('h12', models.BooleanField(default=True)),
                ('i1', models.BooleanField(default=True)),
                ('i2', models.BooleanField(default=True)),
                ('i3', models.BooleanField(default=True)),
                ('i4', models.BooleanField(default=True)),
                ('i5', models.BooleanField(default=True)),
                ('i6', models.BooleanField(default=True)),
                ('i7', models.BooleanField(default=True)),
                ('i8', models.BooleanField(default=True)),
                ('i9', models.BooleanField(default=True)),
                ('i10', models.BooleanField(default=True)),
                ('i11', models.BooleanField(default=True)),
                ('i12', models.BooleanField(default=True)),
                ('j1', models.BooleanField(default=True)),
                ('j2', models.BooleanField(default=True)),
                ('j3', models.BooleanField(default=True)),
                ('j4', models.BooleanField(default=True)),
                ('j5', models.BooleanField(default=True)),
                ('j6', models.BooleanField(default=True)),
                ('j7', models.BooleanField(default=True)),
                ('j8', models.BooleanField(default=True)),
                ('j9', models.BooleanField(default=True)),
                ('j10', models.BooleanField(default=True)),
                ('j11', models.BooleanField(default=True)),
                ('j12', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='multiplex.Movie')),
            ],
        ),
    ]