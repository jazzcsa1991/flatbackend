from rest_framework import serializers
from api.models import PullRequest

#serializer para ver las ramas de un repo
class BranchSerializer(serializers.Serializer):
    branch = serializers.CharField(max_length=200)

#serializer para ver los commits de una rama
class CommitSerializer(serializers.Serializer):
    commit = serializers.CharField()
    message = serializers.CharField()
    author = serializers.CharField()
    date = serializers.CharField()

#serializer para ver el detalle de un commit
class CommitDetailSerializer(serializers.Serializer):
    message = serializers.CharField()
    author = serializers.CharField()
    date = serializers.CharField()
    files = serializers.CharField()
    mail = serializers.CharField()

#serializer para ver los campos de los pull reques de un repo
class PRListSerializer(serializers.Serializer):
    title = serializers.CharField()
    user = serializers.CharField()
    created_at = serializers.CharField()
    state = serializers.CharField()
    number = serializers.CharField()

#serializer para ver el modelo de PR creados
class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PullRequest
        fields = ['author','title','description','status']
    
   
    