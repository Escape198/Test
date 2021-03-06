# Generated by Django 4.0.4 on 2022-06-02 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('DateDel', models.DateField(blank=True, null=True, verbose_name='Delete_date')),
                ('ContactFIO', models.CharField(blank=True, max_length=150, verbose_name='Contact')),
                ('ContactPhone', models.CharField(max_length=12, verbose_name='Phone')),
                ('ContactEmail', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Fname', models.CharField(max_length=50, verbose_name='Surname')),
                ('Date', models.DateField(blank=True, null=True, verbose_name='Date_of_birth')),
                ('Phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Passport', models.CharField(blank=True, max_length=50, null=True, verbose_name='Passport')),
                ('Position', models.IntegerField(blank=True, choices=[(0, 'Admin'), (1, 'Employee'), (2, 'Client')], default=0, null=True, verbose_name='Position')),
                ('Comment', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('NumVU', models.CharField(blank=True, max_length=50, null=True, verbose_name='NumVU')),
                ('Password', models.CharField(blank=True, max_length=150, null=True, verbose_name='Password')),
                ('DateDel', models.DateField(blank=True, null=True, verbose_name='Delete_date')),
                ('CategoryVU', models.JSONField(blank=True, null=True, verbose_name='Categories')),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user_and_company.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
