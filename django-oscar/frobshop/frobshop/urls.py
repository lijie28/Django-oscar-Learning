
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application

# Replace it 4 support oscar
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^music/', include('music.urls')),
    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    #

    url(r'', include(application.urls)),

]
