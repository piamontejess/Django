# Generated by Django 4.0.3 on 2024-06-01 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentEntry', '0005_alter_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]