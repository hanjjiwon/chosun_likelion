from django.contrib import admin
from mainapp.models import Account, Subject_range, Subject_code, Subject, Evaluation



# Register your models here.

admin.site.register(Account)
admin.site.register(Subject_range)
admin.site.register(Subject_code)
admin.site.register(Subject)
admin.site.register(Evaluation)