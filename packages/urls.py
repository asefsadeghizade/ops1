from django.urls import path

from . import views


urlpatterns = [
    path("", views.PackageListAPI.as_view(), name="package_list_api"),
    path("<str:filename>/", views.PackageDownloadAPI.as_view(),
         name="package_download_api")
]
