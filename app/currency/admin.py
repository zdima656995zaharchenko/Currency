from django.contrib import admin
from .models import Source

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'source_url', 'exchange_address', 'phone_number')

admin.site.register(Source, SourceAdmin)


class ContactUsReadOnlyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    fields = '__all__'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False