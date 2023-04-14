from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Ticket
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'setor', 'password1', 'password2')

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('motivo', 'categoria', 'prioridade', 'status', 'nota')

    def __init__(self, *args, is_manager=False, **kwargs):
        super().__init__(*args, **kwargs)
        if not is_manager:
            del self.fields['status']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_manager']  # Adicione ou remova campos conforme necessário