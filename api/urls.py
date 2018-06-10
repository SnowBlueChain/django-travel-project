from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken import views as auth_views

from api import views
from api.modules.city import views as city_views

urlpatterns = [
    # Authentication
    path('sign-up', views.sign_up, name='sign-up'),
    url(r'^api-token-auth/', auth_views.obtain_auth_token),

    # City APIs
    path('get-all-cities', city_views.get_all_cities, name='get-all-cities'),
    path('get-city/<int:city_id>', city_views.get_city, name='get-city'),
    path('get-city-images/<int:city_id>', city_views.get_all_city_images, name='get-city-images'),
    path('get-city-facts/<int:city_id>', city_views.get_all_city_facts, name='get-city-facts'),
]
