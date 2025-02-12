# Generated by Django 5.1.5 on 2025-02-03 13:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_userquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='answer_en',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_en',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(default='Default answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(null=True),
        ),
    ]
