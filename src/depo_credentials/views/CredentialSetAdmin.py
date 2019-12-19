from django.contrib import admin
from depo_credentials.models import CredentialSet
from depo_credentials.views.CredentialSetForm import CredentialSetForm

class CredentialSetAdmin(admin.ModelAdmin):
    form = CredentialSetForm
    
