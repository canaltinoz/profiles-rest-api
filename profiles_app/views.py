from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_app import serializers
from rest_framework import status
from rest_framework import viewsets
from profiles_app import models
from rest_framework.authentication import TokenAuthentication
from profiles_app import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):

    serializer_class=serializers.HelloSerializer

    """Test API View"""

    def get(self,request,format=None):

        """ Returns a list of APIView features"""
        
        an_apiview ={
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'gives you the most control over you appliction logic',
            'is mapped manually URLs',
        }

        return Response({'message':'Hello', 'an_apiview':an_apiview})
    
    def post(self,request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        name=serializer.validated_data.get('name')
        message=f'hello {name}'
        return Response({'message':message})
    
    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """TEST API ViewSets"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset=[
            'uses actions(list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code',
        ]
        return Response({'message ': "Hello !", 'a_viewset':a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        name=serializer.validated_data.get('name')
        message=f'hello {name}'
        return Response({'message':message})
    
    def retrieve(self,request,pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):

    """handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentiction tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating , reading and updating profile feed items"""

    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


        