# Generated by Django 4.0.3 on 2023-03-01 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_questions_alter_answer_question_delete_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
