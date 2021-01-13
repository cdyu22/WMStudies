from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Course, StudentTracker
class UserAdmin(BaseUserAdmin):
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('CRN', 'level','section','course_name','status','followers',)
    fieldsets = (
        (None, {'fields': ('CRN', 'level','section','course_name','status','followers',)}),
        ('Personal info', {'fields': ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('CRN', 'level','section','course_name','status','followers',)}
        ),
    )
    search_fields = ('section',)
    ordering = ('section',)
    filter_horizontal = ()


admin.site.register(Course)



# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)