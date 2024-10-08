from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from newspaper.models import Redactor, Newspaper, Topic


# RedactorForm

class RedactorCreateForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class RedactorUpdateForm(forms.ModelForm):
    username = forms.CharField(
        required=False,
    )
    first_name = forms.CharField(
        required=False,
    )
    last_name = forms.CharField(
        required=False,
    )
    years_of_experience = forms.IntegerField(
        required=False,
    )

    class Meta:
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
            )


# NewspaperForm

class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


# TopicForm

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
