"""bergsolawi URL Configuration

The `urlpatterns` list routes URLs to views.
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin

import juntagrico
import juntagrico_webdav

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"", include("juntagrico.urls")),
    path(r"", include("juntagrico_webdav.urls")),  # FIXME: What to put here?
    path(r"impersonate/", include("impersonate.urls")),
]
