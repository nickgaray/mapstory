from django.conf.urls import url, include

from . import views
from . import api

organization_resource = api.OrganizationResource()

urlpatterns = [
    url(r'^$', views.organization_list, name='list'),
    url(r'^api/', include(organization_resource.urls)),
    url(r'(?P<slug>[-\w]+)/add/layer/(?P<layer_pk>\d+)/$', views.add_layer, name='add_layer'),
    url(r'(?P<slug>[-\w]+)/add/mapstory/(?P<mapstory_pk>\d+)/$', views.add_mapstory, name='add_mapstory'),
    url(r'(?P<slug>[-\w]+)/join/$', views.request_membership, name='request_membership'),
    url(r'(?P<slug>[-\w]+)/manager/$', views.manager, name='manage'),
    url(r'(?P<slug>[-\w]+)/approve/$', views.approve_membership, name='approve_membership'),
    url(r'(?P<slug>[-\w]+)/$', views.organization_detail, name='detail'),
]
