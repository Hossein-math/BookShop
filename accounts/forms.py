from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('national_id', 'mobile_number', 'birth_date')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'mobile_number',
        )