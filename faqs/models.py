
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(default="Default answer")
    question_hi = models.TextField(blank=False, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question

    def get_translated_question(self, lang='en'):
        """Returns the translated question."""
        return getattr(self, f'question_{lang}', self.question)

    def auto_translate(self):
        """translates the question to Hindi and Bengali."""
        translator = Translator()
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        self.save()

    def save(self, *args, **kwargs):
        
        if not self.question_hi or not self.question_bn:
            self.auto_translate()
        super().save(*args, **kwargs)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def get_question_length(self):
        return len(self.question)


class UserQuestion(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question[:50]  #display first 50 chars

from django.db import models


