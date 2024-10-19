from rest_framework.authentication import BaseAuthentication
from job_portal.settings import SECRET_KEY
from accounts.models import Users
from django.core.exceptions import PermissionDenied
import jwt


class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = self.get_token_from_header(auth_header)
            if token:
                try:
                    payload = self.decode_token(token)
                    user_id = payload.get('id')
                    if not user_id:
                        raise PermissionDenied('Invalid token payload')

                    try:
                        user = Users.objects.get(id=user_id)
                        return (user, token)
                    except Users.DoesNotExist:
                        raise PermissionDenied('User not found')

                except jwt.ExpiredSignatureError:
                    raise PermissionDenied('Token has expired')
                except jwt.InvalidTokenError:
                    raise PermissionDenied('Invalid token')

        return None

    def get_token_from_header(self, auth_header):
        parts = auth_header.split()
        if parts[0].lower() != 'bearer':
            raise PermissionDenied('Authorization header must start with Bearer')
        if len(parts) == 1:
            raise PermissionDenied('Token not provided')
        elif len(parts) > 2:
            raise PermissionDenied('Authorization header must be Bearer token')
        return parts[1]

    def decode_token(self, token):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise PermissionDenied('Token has expired')
        except jwt.InvalidTokenError:
            raise PermissionDenied('token is invalid')
