# Generated by Django 4.1 on 2022-08-23 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_emprestimo_data_devolução_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duração',
        ),
    ]
