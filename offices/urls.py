from django.conf.urls import url

from offices.views import OfficeListView

urlpatterns = [
    url(r'^$', OfficeListView.as_view(), name='office-list')
]

