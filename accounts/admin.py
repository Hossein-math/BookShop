from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = [
        'username',
        'mobile_number',
        'email',
        'age',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mobile_number',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('national_id', 'mobile_number', 'birth_date')}),)


admin.site.register(CustomUser, CustomUserAdmin)
