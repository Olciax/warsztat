from django.contrib import admin

from .models import Person
from .models import Address
from .models import Telephone
from .models import Email

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Telephone)
admin.site.register(Email)
# Register your models here.
