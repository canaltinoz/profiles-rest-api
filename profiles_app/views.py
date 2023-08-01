from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_app import serializers
from rest_framework import status

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