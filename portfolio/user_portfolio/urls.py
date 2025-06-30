from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('create',views.create_portfolio,name="create"),
    path('',views.user_home,name="home"),
    path('signup/',views.user_signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('view/<int:ids>',views.portfolio_view,name="view"),
    path('delete/<int:ids>',views.port_delete,name="delete"),
    path('edit/<int:ids>',views.port_edit,name="edit"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)