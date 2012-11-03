from django.db import models

class EmployeeType(models.Model):
	type = models.CharField(max_length = 20)
	def __unicode__ (self):
		return self.type

class Employee(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	type = models.ForeignKey(EmployeeType)
	
	def __unicode__(self):
		return self.first_name + self.last_name
		
class Shift(models.Model):
	start =models.DateTimeField()
	end = models.DateTimeField()
	employee = models.ForeignKey(Employee)
	
	

	
	