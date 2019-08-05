# Generated by Django 2.2 on 2019-08-05 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karya', '0002_auto_20190730_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='assigned_team',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='subtasks',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='subtasks',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='subtasks',
            name='dependent_on',
        ),
        migrations.RemoveField(
            model_name='subtasks',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='EmployeeProfile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='SubTasks',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TeamDetails',
        ),
    ]
