from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {
            'username': ('150 Karakterden uzun olamaz'),
            'email':('Diğer bilgilerle aynı olamaz'),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreate, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})