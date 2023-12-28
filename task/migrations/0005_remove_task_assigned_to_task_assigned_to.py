# Generated by Django 4.2.6 on 2023-12-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_alter_employee_emp_id'),
        ('task', '0004_alter_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(to='users.employee'),
        ),
    ]