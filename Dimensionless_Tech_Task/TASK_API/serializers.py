from TASK_API.models import awsimage
from rest_framework import serializers

class awsimageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = awsimage
        fields = ('image_name','object_name','timestamp','Image','xml_file')