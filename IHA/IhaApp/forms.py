from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import iha_product, iha_property
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        u_email = self.cleaned_data.get('email')
        if User.objects.filter(email=u_email).exists():
            raise ValidationError("Böyle bir Email bulunmaktadır. Başka bir email kullanınız.")
        u_username = self.cleaned_data.get('username')
        if User.objects.filter(username=u_username).exists():
            raise ValidationError("Böyle bir kullanıcı adı bulunmaktadır. Başka bir kullanıcı adı kullanınız.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class IhaCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = iha_product
        fields = '__all__'


class IhaPropertyCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = iha_property
        fields = '__all__'
        exclude = ['iha_Product']

class IhaProductUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = iha_product
        fields = '__all__'
        exclude = ['iha_property']
class IhaPropertyUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = iha_property
        fields = '__all__'
        exclude = ['iha_Product']
