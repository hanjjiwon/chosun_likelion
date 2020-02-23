from django.contrib import admin
from write.models import Account, Subject, Subject_code, Subject_range, Evaluation

admin.site.register(Account)
admin.site.register(Subject_range)
admin.site.register(Subject_code)
admin.site.register(Subject)
admin.site.register(Evaluation)
