from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from formservice.views import *

urlpatterns = patterns('',
                       (r'^$', main_form),
                       (r'^submit/$', process_form)
    # Example:
    # (r'^formservicespike/', include('formservicespike.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
