from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from books import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
        url(r'^hello/$',hello),
        url(r'^time/$',current_datetime),
        url(r'^time/plus/(\d{1,2})/$', hours_ahead),
        (r'^search/$', views.search),
        (r'^contact/$', views.contact),
        (r'^contact/thanks/$', views.thanks),
        (r'^admin/', include(admin.site.urls)),
    )
