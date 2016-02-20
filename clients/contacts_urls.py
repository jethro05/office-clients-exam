from django.conf.urls import url

from clients.views import ContactDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ContactDetailView.as_view(), name='contact-detail')
]

