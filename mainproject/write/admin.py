from django.contrib import admin
from write.models import Subject_range, Subject_code, Subject, Evaluation,Write_index

# Register your models here.
admin.site.register(Subject_range)
admin.site.register(Subject_code)
admin.site.register(Subject)
admin.site.register(Evaluation)
admin.site.register(Write_index)