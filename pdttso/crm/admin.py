import json
import urllib

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.models import Token

from .models import Application

admin.site.site_header = 'Test task CRM'


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'agreement_id', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)
    readonly_fields = ('id', 'created', 'updated')
    change_form_template = 'admin/custom/change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        def payments(self, request, object_id):
            url = "{}/api/v2/agreements/{}/payments/".format(
                settings.BASE_URL, object_id)
            headers = {"Authorization":
                       'Token {}'.format(str(Token.objects.first())),
                       "Accept": 'application/json'}
            try:
                r = urllib.request.Request(url, headers=headers)
                response = urllib.request.urlopen(r)
                data = response.read()
                return json.loads(data)
            except:
                return

        context = {}
        context.update(extra_context or {})
        context.update({'x': payments(self, request, object_id), })
        return super(ApplicationAdmin, self).change_view(request, object_id,
                                                         form_url, context)


admin.site.unregister([Group, User, Token])
admin.site.register(Application, ApplicationAdmin)
