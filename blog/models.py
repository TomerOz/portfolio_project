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

	
	
# a model creation flow:
	# create a model class
	# add model app to the setting
	# make new migrations
	# migrate
	# add to admin