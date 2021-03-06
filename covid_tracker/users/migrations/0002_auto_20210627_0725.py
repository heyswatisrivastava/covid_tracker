# Generated by Django 3.2.4 on 2021-06-27 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.CreateModel(
            name='CovidResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('covid_result', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin_id', to='users.user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_id', to='users.user')),
            ],
            options={
                'db_table': 'covid_results',
            },
        ),
    ]
