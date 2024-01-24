from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю0987654321- '
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел.'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='No choice')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='Not married')

    class Meta:
        model = Women
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')
