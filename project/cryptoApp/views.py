from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile, BlogPost, Comment
from .forms import BlogPostForm, CommentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="loginPage")
def courses(request):
	allPosts = BlogPost.objects.all()
	context = {"courses": allPosts}
	return render(request, "posts.html", context = context)

@login_required(login_url="loginPage")
def home(request):
	return render(request, "home.html", {"user":request.user})

def logoutUser(request):
	logout(request)
	return redirect('loginPage')

def loginPage(request):

	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, "Username OR password is incorrect!")
				return render(request, "login.html")
			


	return render(request, "login.html")

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, "Successfully registered!")
				return redirect('loginPage')
		context = {"form", form}
		return render(request, "register.html", {"form":form})

@login_required(login_url="loginPage")
def course(request):
	return render(request, "course.html")

@login_required(login_url="loginPage")
def quiz(request):
	return render(request, "quiz.html")

@login_required(login_url="loginPage")
def comments(request):
	allPosts = Comment.objects.all()
	context = {"comments": allPosts}
	return render(request, "comments.html", context = context)

@login_required(login_url="loginPage")
def addCourse(request):
	if request.method == "POST":
		currentUser = UserProfile.objects.filter(user = request.user).first()
		form_data = BlogPostForm(data = request.POST)
		if form_data.is_valid():
			post = form_data.save(commit = False)
			post.user = currentUser
			post.save()
			return redirect("courses")
	context = {"form": BlogPostForm}
	return render(request, "addPost.html", context=context)

@login_required(login_url="loginPage")
def addComment(request):
	if request.method == "POST":
		currentUser = UserProfile.objects.filter(user = request.user).first()
		form_data = CommentForm(data = request.POST)
		if form_data.is_valid():
			post = form_data.save(commit = False)
			post.user = currentUser
			post.save()
			return redirect("comments")
	context = {"form": CommentForm}
	return render(request, "addComment.html", context=context)



