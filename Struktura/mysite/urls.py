"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from cart import views as cart_vievs
from user import views as user_vievs
from product import views as product_views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^register/', user_vievs.register_view, name='register'),
    url(r'^login/', user_vievs.login_view, name='user_login'),
    url(r'^index/', cart_vievs.index, name='index'),
    url(r'^logout/', user_vievs.logout_view, name='user_logout'),
    url(r'^newcart/', cart_vievs.new_cart_view, name='newcart'),
    url(r'^structure/', cart_vievs.show_cart, name='cart_structure'),
    url(r'^cart/', product_views.new_product_view, name='cart'),
    url(r'^cart/', product_views.show_products_by_cart, name='cart'),




]
