from django.contrib import admin
from write.models import Subject_range, Subject_code, Subject, Evaluation

# Register your models here.

admin.site.register(Subject_range)
admin.site.register(Subject_code)
admin.site.register(Subject)
admin.site.register(Evaluation)