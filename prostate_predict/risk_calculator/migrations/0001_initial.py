# Generated by Django 3.0.5 on 2020-04-20 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person_Inputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('brothers', models.PositiveSmallIntegerField()),
                ('sisters', models.PositiveSmallIntegerField()),
                ('older_brothers', models.PositiveSmallIntegerField()),
                ('older_sisters', models.PositiveSmallIntegerField()),
                ('dark_skin', models.BooleanField()),
                ('past_cancer', models.BooleanField()),
                ('past_breast_cancer', models.BooleanField()),
                ('past_other_cancer', models.BooleanField()),
                ('father_prostate', models.BooleanField()),
                ('mother_breast', models.BooleanField()),
                ('brother_prostate', models.PositiveSmallIntegerField()),
                ('sister_prostate', models.PositiveSmallIntegerField()),
                ('mutation', models.BooleanField()),
                ('psa', models.FloatField()),
                ('volume_prostate', models.FloatField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('low_testosterone', models.BooleanField()),
                ('sexual_difficulties', models.BooleanField()),
                ('heat', models.BooleanField()),
                ('medicine_fin_dist', models.BooleanField()),
                ('medicine_erection', models.BooleanField()),
                ('medicine_cholesterol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Person_Results',
            fields=[
                ('person_inputs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='risk_calculator.Person_Inputs')),
                ('psa_andro_corr', models.FloatField()),
                ('psa_density', models.FloatField()),
                ('psa_density_corr', models.FloatField()),
                ('genetic_risk', models.FloatField()),
                ('family_pertinence', models.FloatField()),
                ('family_info', models.FloatField()),
                ('apparente_one', models.PositiveSmallIntegerField()),
                ('irm_to_realise', models.BooleanField()),
                ('general_pop_risk', models.FloatField()),
                ('individual_risk', models.FloatField()),
            ],
        ),
    ]
