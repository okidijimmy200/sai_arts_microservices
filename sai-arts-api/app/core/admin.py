from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models

class UserAdmin(BaseUserAdmin):
    # change the ordering of the id of object
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', )}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login', )})

    )

        # customize field set to accommodate password and email
    add_fieldsets = (
        (None, { 
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
         }),
    )
    def has_module_permission(self, request):
        return True

admin.site.register(models.User, UserAdmin)