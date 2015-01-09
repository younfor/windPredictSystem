from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from wind.models import UserProfile
from wind import models
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'is_staff')
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'userprofile', None) is None:
            print 'userprofile is null',request.user.userprofile
            obj.save()
            u=UserProfile()
            u.user=obj
            u.father=request.user.userprofile
            u.save()
            obj.userprofile = u
        print 'save model'
        obj.save()
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        print 'ps:get_queryset'
        # If super-user, show all 
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
