# Generated by Django 2.2.6 on 2019-11-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('manager', 'manager com'), ('hr', 'hr com'), ('programmer', 'programmer inc'), ('programmer trainee', 'programmer_trainee com'), ('others', 'others com')], max_length=50)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'company_employee_details',
            },
        ),
    ]
