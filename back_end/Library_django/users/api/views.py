from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers

class RegisterAPIView(generics.CreateAPIView):
    
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = (permissions.AllowAny, )

#..............................................................................................................
class LoginAPIView(APIView):
    
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        return ObtainAuthToken().post(request)
    

# #.................................................................................................................
# @api_view(['POST'])
# def login_user(request):
#     if request.method == "POST":
#         username = request.data["username"]
#         password = request.data["password"]
#                 
#         user = authenticate(username=username, password=password)
#         if user:            
#             serializer = LoginUserSerializer(user)
#             return Response(serializer.data, status=HTTP_200_OK)
#             
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   
#             
            
            
