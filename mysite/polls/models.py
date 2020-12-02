
# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # It’s important to add __str__() methods to the models, not only for your own convenience when dealing with the
    # interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated
    # admin.
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text