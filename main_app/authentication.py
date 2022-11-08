from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
# Retrieving our User model in the variable below
User = get_user_model()

class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request):
        # Grabbing the authorization header from the request
        header = request.headers.get('Authorization')
        # exiting if the header does not exist
        if not header:
            return None
        # throwing an error if the header does not start with the word Bearer 
        if not header.startswith('Bearer'):
            raise PermissionDenied({'message': 'Invalid Authorization header!'})
        # Grabbing the token from the header
        token = header.replace('Bearer ', '')

        try: 
        # Decode token and fetch associated user
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        # Throw an error if the token is invalid
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'message': 'Invalid Token'})
        # Throw an error if the User does not exist/cannot find user
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'User not found'})
        # Finally, if everything goes well, return a tuple with the user and token elements
        return (user, token)
        



