"""
URL configuration for auto_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import path, include

import store.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("password-reset/", store.views.ResetPasswordView.as_view(), name="password_reset"),
    path(
            "forgot_password/confirm/<uidb64>/<token>/",
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', success_url='/login/'),
            name="password_reset_confirm",
        ),
    path("activate/<user_signed>", store.views.activate, name="activate")
]
