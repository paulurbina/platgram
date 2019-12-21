# Django
from django.contrib import admin
from django.contrib.auth import UserAdmin as BaseUserAdmin
# Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  
  list_display = ('pk', 'user', 'website', 'phone_number', 'picture')
  list_display_links = ('pk', 'user')
  list_editable = ('website', 'phone_number', 'picture')
  search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')

  list_filter = (
    'created', 
    'modified',
    'user__is_active',
    'user__is_staff')

  fieldsets = (
    ('Profile', {
      'fields': (('user', 'picture'),),
    }),
    ('Extra info', {
      'fields': (
        ('website', 'phone_number'),
        ('bigoraphy')
      )
    }),
    ('Metatada', {
      'fields': (('created', 'modified'),),
    })
  )

  readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name_plural = 'profiles'

  
