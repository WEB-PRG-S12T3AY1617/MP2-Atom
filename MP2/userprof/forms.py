from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from . models import Post, Offers

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = True, help_text = 'Required.')
    last_name = forms.CharField(max_length = 30, required = True, help_text = 'Required.')
    email = forms.EmailField(max_length = 254, help_text = 'Required. Inform a valid email address.')
    # password =  forms.CharField(widget = forms.PasswordInput)
    degree = forms.CharField(help_text = 'Enter your degree/office. Whatever you input here will be set to your profile.')

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'degree' ,'email', 'password1', 'password2']
        help_texts = {
            'password1': _('Your password cannot be too similar to your other personal information. Your password must contain at least 8 characters. Your password cannot be a commonly used password. Your password cannot be entirely numeric.'),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['item_name', 'quantity', 'thumbnail', 'tags']

class purchaseOfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['amount',]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(purchaseOfferForm, self).__init__(*args, **kwargs)

class tradeOfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['item',]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(tradeOfferForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Post.objects.filter(op__id=self.user.id)
