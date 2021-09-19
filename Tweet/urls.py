
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('register/', user_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html') , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html') , name='logout'),
    path('profile/', user_view.profile , name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

