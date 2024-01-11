# Generated by Django 4.2.1 on 2024-01-10 13:56

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_employee_profile_pic_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default=users.models.generate_emp_id, editable=False, max_length=50),
        ),
    ]
