
# Create your models here.

import datetime
from django.db import models
from django.utils import timezone

class Meta:
    app_label  = 'polls'

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # It’s important to add __str__() methods to the models, not only for your own convenience when dealing with the
    # interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated
    # admin.
    def __str__(self):
        return self.question_text

    # def create_question(question_text, days):
    #     """
    #     Create a question with the given `question_text` and published the
    #     given number of `days` offset to now (negative for questions published
    #     in the past, positive for questions that have yet to be published).
    #     """
    #     time = timezone.now() + datetime.timedelta(days=days)
    #     return Question.objects.create(question_text=question_text, pub_date=time)


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text