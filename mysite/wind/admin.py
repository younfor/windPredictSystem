from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import forms
from django.contrib.auth.models import User
from wind.models import UserProfile
from wind import models
from django.utils.translation import ugettext, ugettext_lazy as _
# which acts a bit like a singleton
from django.contrib.auth import forms


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

    def get_fields(self, request, obj=None):
        form = super(UserProfileInline, self).get_formset(
            request, obj, fields=None).form
        # if 'level' in form.base_fields:
        #   print 'yes level'
        # else:
        #   print 'no level'
        return list(form.base_fields) + list(self.get_readonly_fields(request, obj))

# Define a new User admin


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'is_staff', 'get_UserProfile')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_UserProfile(self,obj):
        return obj.userprofile

    def get_form(self, request, obj=None, **kwargs):
        # Get form from original UserAdmin.
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        # here is according to the system
        if 'user_permissions' in form.base_fields:
            permissions = form.base_fields['user_permissions']
            permissions.queryset = permissions.queryset.filter(
                content_type__name='log entry')
        return form

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'userprofile', None) is None:
            print 'userprofile is null', request.user.userprofile
            obj.save()
            u = UserProfile()
            u.user = obj
            u.father = request.user.userprofile
            u.save()
            obj.userprofile = u
        print 'save model'
        obj.save()

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        print 'ps:get_queryset'  # If super-user, show all
        if request.user.is_superuser:
            return qs
        return qs.filter(userprofile__father=request.user.userprofile)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# register Models
admin.site.register(models.PowerStation)
admin.site.register(models.Factory)
admin.site.register(models.WindTurbine)
admin.site.register(models.PowerData)
