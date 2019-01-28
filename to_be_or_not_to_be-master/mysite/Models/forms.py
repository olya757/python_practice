from django.contrib.auth.forms import *
from .models import *
from django import forms


class TeacherCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username','name','surname','name','second_name')


class TeacherChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username','name','surname','name','second_name')


class GroupCurriculumSearchForm(forms.Form):
    group_curriculum = forms.ModelChoiceField(label='Курс обучения', queryset=GroupCurriculum.objects.filter())
    datetime = forms.DateTimeField(label='Дата')

