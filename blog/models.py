from django.db import models

class Blog(models.Model):
	# text
	title = models.CharField(max_length=255)
	# publication date
	pubish_date = models.DateTimeField()
	# body
	text = models.TextField(max_length=800)
	# image
	image = models.ImageField(upload_to='images/')
	
	def summary(self):
		short_text = self.text[:100]
		if len(self.text)>100:
			short_text = short_text + '...'
		return short_text
		
	def pub_date_pretty(self):
		return self.pubish_date.strftime('%b %e %y')
		
	def __str__(self):
		return self.title

	
	
# a model creation flow:
	# create a model class
	# add model app to the setting
	# make new migrations
	# migrate
	# add to admin