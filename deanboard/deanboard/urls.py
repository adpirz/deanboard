from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('referrals.urls')),
    url(r'^referrals/', include('referrals.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('students.urls')),
    url(r'^scholars/', include('students.urls')),
)
