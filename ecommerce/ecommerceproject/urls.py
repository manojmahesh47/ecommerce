from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shopapp.views import allProdCat, proDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('', allProdCat, name='all_products'),
    path('<c_slug>/<product_slug>/', proDetail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
