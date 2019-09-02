from django.db import models

class Blog(models.Model):
	text = models.TextField(max_length=400)