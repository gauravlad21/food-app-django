from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('foodmenu.urls')),
    path('register/', users_views.register, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', users_views.profile_page, name='profile')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
