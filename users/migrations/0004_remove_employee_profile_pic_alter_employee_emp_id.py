# Generated by Django 4.2.1 on 2024-01-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_employee_first_name_remove_employee_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='E303D8A093', editable=False, max_length=50),
        ),
    ]
