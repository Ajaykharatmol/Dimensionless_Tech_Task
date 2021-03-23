from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .models import awsimage
from .serializers import awsimageSerializers

class GetImagefileDetails(APIView):
    #permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def get(self,reuest):
        qs = awsimage.objects.all()
        serializer = awsimageSerializers(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

      file_serializer = awsimageSerializers(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response({
              "Image": file_serializer.data,
              "message": "created successfully!",
              "status code": status.HTTP_201_CREATED
          }, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return awsimage.objects.get(pk=pk)
        except awsimage.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def patch(self, request, pk):
        qs = self.get_object(pk)
        try:
            serializer = awsimageSerializers(qs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Image": serializer.data,
                    "message": "updated successfully!",
                    "status": status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors)

    def delete(self, request, pk):
        qs = self.get_object(pk)
        qs.delete()
        return Response({"message": "Record has been deleted!"}, status=status.HTTP_200_OK)


