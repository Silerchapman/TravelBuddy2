from django.conf.urls import url, include
from . import views


urlpatterns =[
	#sets dashboard as home page in travels dir 
	url(r'^$', views.travel_index, name= 'travel_index'),

    url(r'^create$', views.add_item, name= 'add' ),
    url(r'^create_item$', views.create_item, name= 'create'),
    url(r'^logout$', views.logout, name= 'logout' ),
    url(r'^destination/(?P<item_id>\d+)$', views.view_trip, name= 'view'), 
    

    url(r'^add/(?P<item_id>\d+)$', views.add_wishlist, name= 'add_wishlist')


]