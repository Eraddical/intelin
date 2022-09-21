from django import forms
from intelin.models import Argument, Refute


class ArgumentForm(forms.ModelForm):
    class Meta:
        model = Argument
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '본론',
        }


class RefuteForm(forms.ModelForm):
    class Meta:
        model = Refute
        fields = ['content']
        labels = {
            'content': '본론',
        }
