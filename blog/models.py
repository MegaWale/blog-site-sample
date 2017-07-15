from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
	STATUS_CHIOCES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	title = models.Charfield(max_length=250)
	slug = models.SlugField(max_length=250,
							unique_for_date='publish')
	author = models.ForeignKey(User,
								related_name='blog_post')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.Charfield(max_length=10,
								chioce=STATUS_CHIOCES,
								default='draft')
	
	class meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


