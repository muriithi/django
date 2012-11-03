import models
from django.contrib import admin


admin.site.register(models.Shift)
admin.site.register(models.EmployeeType)

class EmployeeAdmin(admin.ModelAdmin):
	fields = ['first_name','last_name', 'type']
	list_display = ('first_name','last_name', 'type')
	
admin.site.register(models.Employee, EmployeeAdmin)	