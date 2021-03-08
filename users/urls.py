from django.conf.urls import url
from users import views

urlpatterns = [
    url('^$', views.customer_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
