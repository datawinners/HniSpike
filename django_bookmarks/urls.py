import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
    # Example:
    # (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', main_page),
    (r'^user/(\w+)/$',user_page),
    (r'^login/$','django.contrib.auth.views.login'),
    (r'^logout/$',logout_page),
    (r'^register/$','bookmarks.views.register_page'),
    (r'^export/$','bookmarks.views.export_bookmarks_to_csv'),
    (r'^register/success/$',direct_to_template,{'template':'registration/register_success.html'}),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':site_media}),

)
