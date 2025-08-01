from django.shortcuts import render

import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404


class PackageListAPI(APIView):
    def get(self, request):
        try:
            files = os.listdir(settings.MEDIA_ROOT)
            packages = [
                {
                    "filename": f,
                    "download_url": request.build_absolute_uri(f"{f}")
                }
                for f in files if f.endswith(".whl") or f.endswith(".tar.gz")
            ]
        except FileNotFoundError:
            packages = []

        return Response(packages)


class PackageDownloadAPI(APIView):
    def get(self, request, filename):
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        raise Http404("Package not found")
