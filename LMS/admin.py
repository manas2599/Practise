from django.contrib import admin
from LMS.models import studentdetails
from LMS.models import Courses
from LMS.models import Assignment
from LMS.models import Marks
# Register your models here.
admin.site.register(studentdetails)
admin.site.register(Courses)
admin.site.register(Assignment)
admin.site.register(Marks)