from django.db import models

class Employee(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	basic_salary = models.DecimalField(max_digits = 12,decimal_places=2)
	department = models.CharField(max_length = 30)
	