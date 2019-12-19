from django.contrib import admin
from depo_credentials.views.CredentialSetAdmin import CredentialSetAdmin
from depo_credentials.models.CredentialSet import CredentialSet

# Register your models here.
admin.site.register(CredentialSet, CredentialSetAdmin)