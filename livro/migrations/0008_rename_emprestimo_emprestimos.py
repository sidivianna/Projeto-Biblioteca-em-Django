# Generated by Django 4.1 on 2022-08-23 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0007_remove_emprestimo_tempo_duração'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emprestimo',
            new_name='Emprestimos',
        ),
    ]