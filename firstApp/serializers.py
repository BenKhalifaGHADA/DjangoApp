from rest_framework import serializers
from .models import Task
class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','title','description','status','assigned_to']
        read_only_fields=['id','assigned_to']