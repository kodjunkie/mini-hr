from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm as BaseCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserCreationForm(BaseCreationForm):
    class Meta(BaseCreationForm.Meta):
        model = User
        fields = BaseCreationForm.Meta.fields + (
            'dob', 'address', 'phone', 'country',
            'state', 'city', 'avatar', 'position',
            'marital_status', 'work_status', 'date_employed',
            'work_type', 'bio', 'department'
        )


class UserAdmin(BaseUserAdmin):
    # The form to add a user
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    list_display = ('fullname', 'email', 'department', 'work_status', 'position', 'work_type')
    list_filter = ('department', 'work_status')
    fieldsets = (
        ('Personal',
         {'fields': ('avatar', 'first_name', 'last_name', 'phone', 'email', 'dob', 'gender', 'marital_status', 'bio')}),
        ('Authentication', {'fields': ('username', 'password')}),
        ('Work Info', {'fields': ('position', 'work_status', 'work_type', 'department', 'date_employed')}),
        ('Residence', {'fields': ('address', 'city', 'state', 'country')})
    )
    add_fieldsets = (
        ('Authentication', {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),
    )
    search_fields = ('email', 'phone', 'department', 'position')
    ordering = ('first_name',)


admin.site.register(User, UserAdmin)
