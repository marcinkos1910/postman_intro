## Postman
tbp

## Serializers
tbd

# DRF setup
## Django Rest Framework project setup guide

1. ```pipenv shell --python 3.10 / mkvirtualenv drf --python 3.10```

2. ```pipenv / pip install django django-debug-toolbar djangorestframework drf-yasg```

3. ```mkdir drf```

4. ```cd drf```

5. ```django-admin startproject config .```

6. ```python manage.py startapp user```

7. user.models

```python
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
```

8. user.admin

```python
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user import models


class CustomUserAdmin(UserAdmin):
    model = get_user_model()


admin.site.register(models.CustomUser, CustomUserAdmin)
```

9. config.settings

```python
INSTALLED_APPS = [
    "debug_toolbar",
    "rest_framework",
    "drf_yasg",

    "user.apps.UserConfig",
]
```

10. config.settings

```python
AUTH_USER_MODEL = 'user.CustomUser'
```

11. config.settings

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

12. config.settings

```python
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # The end of middleware
]
```

13. config.urls

```python
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api-auth/", include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
```

14. config.settings

```python
if DEBUG:
    import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']
```

15. config.urls  

```python
# Rename Admin Page
admin.site.site_title = "DjangoRestFramework Training"
admin.site.site_header = "DjangoRestFramework Training"
admin.site.index_title = "DjangoRestFramework Training"
```