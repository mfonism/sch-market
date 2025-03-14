# Generated by Django 3.1.3 on 2021-03-25 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('badge', models.ImageField(blank=True, null=True, upload_to='assets/badge')),
                ('school_type', models.CharField(choices=[('Boarding', 'Boarding'), ('Day', 'Day'), ('Both', 'Both')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Mixed', 'Mixed')], max_length=20)),
                ('level', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Both', 'Both')], max_length=40)),
                ('state', models.CharField(max_length=100)),
                ('date_established', models.DateTimeField(blank=True, null=True)),
                ('curriculum', models.CharField(max_length=255)),
                ('school_fees_range', models.CharField(max_length=255)),
                ('extra_curriculum_activities', models.TextField()),
                ('school_phone_number', models.CharField(max_length=25)),
                ('school_email', models.EmailField(max_length=254)),
                ('motto', models.CharField(max_length=255)),
                ('website', models.URLField(blank=True, null=True)),
                ('clubs', models.TextField()),
                ('awards_won', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'School Profile',
                'verbose_name_plural': 'School Profile',
                'ordering': ('school_name', 'created'),
            },
        ),
    ]
