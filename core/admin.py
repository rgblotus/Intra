from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model



from .forms import CustomUserCreationForm, CustomUserChangeForm 

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','mobile_number','is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = [
        (
            None,
            {
                'fields': ['username', 'email', ('first_name', 'last_name'), 'mobile_number','last_login', 'date_joined'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'fields': ['password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                'fields': ['username', 'email', ('first_name', 'last_name'), 'mobile_number','password1', 'password2'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],

                'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
            },
        ),
    ]
    search_fields = ('username', 'first_name', 'last_name', 'mobile_number')
    ordering = ('username', 'date_joined', 'last_login')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
