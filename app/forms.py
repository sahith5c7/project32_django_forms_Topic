from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()


class WebpageForm(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    n1=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=n1)
    author=forms.CharField()
    date=forms.DateField()
