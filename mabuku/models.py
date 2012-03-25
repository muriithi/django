from django.db import models

class Book(models.Model):
	title = models.CharField(max_length = 50)
	edition = models.CharField(max_length = 20)
	isbn =models.CharField(max_length = 20)
	authors = models.ManyToManyField('Author')
	purchase_date = models.DateField()
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		ordering =['title']
	
	
class Author(models.Model):
	first_name = models.CharField(max_length = 50)
	middle_name = models.CharField(max_length =50, blank = True)
	last_name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return u'%s %s' %(self.first_name, self.last_name)
	
