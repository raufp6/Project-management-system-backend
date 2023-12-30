# Generated by Django 4.2.6 on 2023-12-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_alter_employee_emp_id'),
        ('task', '0007_file_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='task_of', to='users.employee'),
        ),
    ]