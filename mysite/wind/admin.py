from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import forms
from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import User
from wind.models import UserProfile
from wind import models
from django.utils.translation import ugettext, ugettext_lazy as _
# which acts a bit like a singleton
from django.contrib.auth import forms
from django.contrib.admin.util import flatten_fieldsets
from django.contrib.auth.models import Group
from django.db.models import F, Q
from django.utils.functional import curry
from django import forms


class ReadOnlyAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if request.user.userprofile.level == '1':
            return self.model._meta.get_all_field_names()
        else:
            return []

    def has_add_permission(self, request):
        # Nobody is allowed to add
        if request.user.userprofile.level == '1':
            return False
        else:
            return super(ReadOnlyAdmin, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        if request.user.userprofile.level == '1':
            return False
        else:
            return super(ReadOnlyAdmin, self).has_delete_permission(request)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fieldsets = (
        (None, {
            'fields': (
                ('telephone',),
                ('address',),
                ('level',),
                ('father',),
            ),
        }),
    )

    def get_fields(self, request, obj=None):
        # readonly for system_user
        if request.user.userprofile.level == '1':
            self.readonly_fields = ['level', 'address', 'telephone', 'father']
        # form
        form = super(UserProfileInline, self).get_formset(
            request, obj, fields=None).form
        # if 'level' in form.base_fields:
        #   print 'yes level'
        # else:
        #   print 'no level'
        return list(form.base_fields) + list(self.get_readonly_fields(request, obj))

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['father', 'level']
        else:
            return []

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        level = int(request.user.userprofile.level) + 1
        if level == 1:
            level = level + 1
        if request.method == "GET":
            initial.append({
                'level': level,
                'father': request.user.userprofile,
            })
        formset = super(UserProfileInline, self).get_formset(
            request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset


class UserAdmin(UserAdmin, ReadOnlyAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'is_staff', 'level', 'father')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser',
                                       )}),
        #(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def father(self, obj):
        return obj.userprofile.father

    def level(self, obj):
        return obj.userprofile.level

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
        print 'add default group'
        g = Group.objects.get(name='default')
        obj.save()
        obj.groups.add(g)

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        print 'ps:get_queryset'  # If super-user, show all
        if (request.user.userprofile.level == '0') or (request.user.userprofile.level == '1'):
            return qs
        else:
            return qs.filter(Q(userprofile__father=request.user.userprofile)
                             | Q(userprofile=request.user.userprofile))

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        if request.user.userprofile.level != '0' and request.user.userprofile.level == obj.userprofile.level:
            return ['username']
        else:
            return []


class FactoryAdmin(ReadOnlyAdmin):

    list_display = ('name', 'user', 'begintime', 'endtime', 'scope')

    def get_queryset(self, request):
        qs = super(FactoryAdmin, self).get_queryset(request)
        if (request.user.userprofile.level == '0') or (request.user.userprofile.level == '1'):
            return qs
        else:
            return qs.filter(Q(user=request.user))

    def has_add_permission(self, request):
        # Nobody is allowed to add
        if request.user.userprofile.level != '0':
            return False
        else:
            return super(ReadOnlyAdmin, self).has_add_permission(request)

    def get_readonly_fields(self, request, obj=None):
        rs = super(FactoryAdmin, self).get_readonly_fields(request, obj)
        if request.user.userprofile.level != '0':
            return ['scope', 'begintime', 'endtime', 'user']
        else:
            return []


class PowerAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PowerAdminForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['user'].queryset = User.objects.filter(
            userprofile__level__gt='2')


class PowerStationAdmin(ReadOnlyAdmin):
    form = PowerAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(PowerStationAdmin, self).get_form(request, obj, **kwargs)
        factory = models.Factory.objects.get(
            user=request.user)
        form.base_fields['factory'].initial = factory
        form.base_fields['begintime'].initial = factory.begintime
        form.base_fields['endtime'].initial = factory.endtime
        return form


class TurbineAdmin(ReadOnlyAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(TurbineAdmin, self).get_form(request, obj, **kwargs)
        power = models.PowerStation.objects.get(
            user__userprofile__father=request.user.userprofile)
        form.base_fields['powerstation'].initial = power
        form.base_fields['begintime'].initial = power.begintime
        form.base_fields['endtime'].initial = power.endtime
        return form


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# register Models
admin.site.register(models.PowerStation, PowerStationAdmin)
admin.site.register(models.Factory, FactoryAdmin)
admin.site.register(models.WindTurbine, TurbineAdmin)
admin.site.register(models.PowerData, ReadOnlyAdmin)
