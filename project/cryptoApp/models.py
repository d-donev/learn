from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique = True, on_delete = models.CASCADE)
	user_biography = models.TextField(default = 'none')
	def __str__(self):
		return self.user.username


class BlogPost(models.Model):
	title = models.CharField(max_length = 50)
	user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
	content = models.TextField(null = True, blank = True)
	date_created = models.DateField()
	last_changed = models.DateField()
	def __str__(self):
		return self.title + " " + self.user.user.username

class Comment(models.Model):
	title = models.CharField(max_length = 50)
	user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
	content = models.TextField(null = True, blank = True)
	date_created = models.DateField()
	def __str__(self):
		return self.title + " " + self.user.user.username



