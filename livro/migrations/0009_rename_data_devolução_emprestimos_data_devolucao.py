# Generated by Django 4.1 on 2022-08-23 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_rename_emprestimo_emprestimos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='data_devolução',
            new_name='data_devolucao',
        ),
    ]
