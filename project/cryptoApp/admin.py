from django.contrib import admin
from .models import UserProfile, BlogPost, Comment
from django.contrib.auth.models import User
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_biography')
	def has_remove_permission(self, request, obj=None):
		return True
	def has_add_permission(self, request, obj=None):
		return True
	def has_change_permission(self, request, obj=None):
		if obj is not None and obj.user != request.user:
			return False
		else:
			return True
admin.site.register(UserProfile, UserProfileAdmin)



class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'user',)
	search_fields = ['title', 'content']
	list_filter = (('date_created', DateTimeRangeFilter),)
	exclude = ('user',)
	def has_add_permission(self, request, obj=None):
		return True
	def has_change_permission(self, request, obj=None):
		return True
	def save_model(self, request, obj, form, change):
		userP = UserProfile.objects.filter(user=request.user).first()
		if userP is None:
			u = UserProfile.objects.create(user=request.user,user_biography="None")
			obj.user = u
		else:
			obj.user = userP
		super().save_model(request, obj, form, change)
	def save_formset(self, request, form, formset, change):
		userP = UserProfile.objects.filter(user = request.user).first()
		instances = formset.save(commit=False)
		for instance in instances:
			instance.user = userP
			instance.save()
		formset.save()
	def get_readonly_fields(self, request, obj=None):
		userP = UserProfile.objects.filter(user = request.user).first()
		if obj is None:
			return []
		if obj is not None and obj.user == userP:
			return []
		return ['title', 'user', 'content', 'date_created', 'last_changed']
admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'user',)
	search_fields = ['content', 'content']
	list_filter = (('date_created', DateTimeRangeFilter),)
	exclude = ('user','title')
	def has_add_permission(self, request, obj=None):
		return True
	def has_change_permission(self, request, obj=None):
		return True
	def save_model(self, request, obj, form, change):
		userP = UserProfile.objects.filter(user=request.user).first()
		if userP is None:
			u = UserProfile.objects.create(user=request.user,user_biography="None")
			obj.user = u
		else:
			obj.user = userP
		super().save_model(request, obj, form, change)
	def save_formset(self, request, form, formset, change):
		userP = UserProfile.objects.filter(user = request.user).first()
		instances = formset.save(commit=False)
		for instance in instances:
			instance.user = userP
			instance.save()
		formset.save()
	def get_readonly_fields(self, request, obj=None):
		userP = UserProfile.objects.filter(user = request.user).first()
		if obj is None:
			return []
		if obj is not None and obj.user == userP:
			return []
		return ['title', 'user', 'content', 'date_created']
admin.site.register(Comment, CommentAdmin)

