# Generated by Django 4.1 on 2022-08-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolução',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='tempo_duração',
            field=models.DateField(blank=True, null=True),
        ),
    ]
