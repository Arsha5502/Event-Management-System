# Generated by Django 4.2.5 on 2023-09-13 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_applicant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='fname',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='phone',
            new_name='Phone',
        ),
    ]
