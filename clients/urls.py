from django.conf.urls import url

from clients.views import ClientListView, ClientDetailView

urlpatterns = [
    url(r'^$', ClientListView.as_view(), name='client-list'),
    url(r'^(?P<pk>\d+)/$', ClientDetailView.as_view(), name='client-detail')
]
