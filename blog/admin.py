from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Comment


@admin.register(User)
class RegisterUserAdmin(UserAdmin):
    model = User

    list_display = (
        'username',
        'email',
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    
    search_fields = (
        'username',
        'email',
    )

   
    ordering = ('username',)

    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'phone_number',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)