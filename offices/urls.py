from django.conf.urls import url

from offices.views import OfficeListView, OfficeDetailView

urlpatterns = [
    url(r'^$', OfficeListView.as_view(), name='office-list'),
    url(r'^(?P<pk>\d+)/$', OfficeDetailView.as_view(), name='office-detail')
]

