from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from .views import views
from .views import booking


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gallery/', views.gallery_view, name='gallery'),
    url(r'^reservation/', booking.reservation_view, name='booking'),
    url(r'^contact_us', views.contact_us, name='contact_us'),
    url(r'^about_us', views.about_us, name='about-us'),
    url('admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^food/', include('food.urls', namespace='food')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)