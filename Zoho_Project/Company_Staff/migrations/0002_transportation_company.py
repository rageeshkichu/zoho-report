# Generated by Django 3.2.25 on 2024-05-11 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails'),
        ),
    ]
