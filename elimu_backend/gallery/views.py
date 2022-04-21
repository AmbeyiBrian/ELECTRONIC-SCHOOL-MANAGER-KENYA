from rest_framework.response import Response
from rest_framework.views import APIView
from gallery.models import Gallery
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from gallery.serializers import GetSerializer, PostSerializer


class PostAPI(APIView):
    permission_classes = ()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

    def get(self, school, request):
        galleryPhotos = Gallery.objects.filter(school=school)
        serializer = GetSerializer(galleryPhotos, many=True)
        return Response(serializer.data)


class GetAPI(APIView):
    permission_classes = ()
    serializer_class = GetSerializer

    def get(self, request, school):
        galleryPhotos = Gallery.objects.filter(school=school)
        serializer = GetSerializer(galleryPhotos, many=True)
        return Response(serializer.data)


class DeleteAPI(APIView):
    permission_classes = ()
    serializer_class = GetSerializer

    def delete(self, request, id, format=None):
        photo = Gallery.objects.get(id=id)
        photo.delete()
        serializer = GetSerializer(photo)
        return Response(serializer.data)
