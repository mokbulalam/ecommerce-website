"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


from . import views
import accounts.views
from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name="about_page"),
    path('login/', accounts.views.login_page, name="login_page"),
    path('register/', accounts.views.register_page, name="register_page"),
    path('logout/', accounts.views.logout_page, name="logout_page"),

    path('', ProductListView.as_view()),
    path('products/', include(("products.urls", "products"), namespace='products')),
    path('cart/', include(("carts.urls", "carts"), namespace='cart')),
    path('search/', include(("search.urls", "search"), namespace='search')),

    ###################### API url #######################
    path('api/', include(("api.urls", "api"), namespace='api')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
