from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BlogPost, Comment
from django.shortcuts import render, redirect


class BlogPostForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BlogPostForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control mb-3"
	class Meta:
		model = BlogPost
		exclude = ("user",)

class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control mb-3"
	class Meta:
		model = Comment
		exclude = ("user","title")

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","email", "password1", "password2"]
