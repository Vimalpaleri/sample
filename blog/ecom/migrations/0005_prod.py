# Generated by Django 2.2.6 on 2020-01-15 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_auto_20200115_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='prod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('catogeryy', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('categorys', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecom.category')),
            ],
            options={
                'db_table': 'ecom_product',
            },
        ),
    ]
