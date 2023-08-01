from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
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
    