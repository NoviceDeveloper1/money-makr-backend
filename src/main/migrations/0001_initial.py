# Generated by Django 3.1.2 on 2020-10-04 19:58

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Others', max_length=63, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=127, populate_from=['name'])),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_category', to='main.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True)),
                ('budget_goal', models.FloatField(default=0)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=127, populate_from=['name'])),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('wallet_type', models.CharField(default='liquid_assets', max_length=63)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=127, populate_from=['name', 'wallet_type'])),
                ('currency', models.CharField(max_length=7)),
                ('balance', models.FloatField(default=0)),
                ('exclude_from_total', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('name', 'wallet_type')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('transaction_type', models.IntegerField(choices=[(1, 'Income'), (-1, 'Expense')])),
                ('date', models.DateField()),
                ('exclude_from_report', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default='Others', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.event')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.wallet')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_goal', models.FloatField(default=0)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('category', models.ForeignKey(default='Others', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category')),
            ],
        ),
    ]
