# Generated by Django 3.2.8 on 2021-11-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
    ]
