from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	story = models.TextField(max_length=200,blank=True,null=True)
	link = models.URLField(max_length=200,blank=True,null=True)
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
	pub_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title