from re import template
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView , RedirectView

# 앱 url 호출
urlpatterns = [
    #path('', TemplateView.as_view(template_name='root.htm'), name='root'),
    path('', RedirectView.as_view(
        #url='/instagram/'
            pattern_name='instagram:post_list'
        ), name='root'),
        
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]