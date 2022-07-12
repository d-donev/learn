
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cryptoApp.views import courses, addCourse, comments, addComment, home, course, quiz, register, loginPage, logoutUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='loginPage'),
    path('logout/', logoutUser, name='logout'),
    path('course/', course, name='course'),
    path('quiz/', quiz, name='quiz'),
    path('courses/', courses, name='courses'),
    path('add/course/', addCourse, name="addCourse"),
    path('comments/', comments, name='comments'),
    path('add/comment/', addComment, name="addComment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)