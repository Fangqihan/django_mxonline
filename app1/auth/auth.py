from app1.models import Token
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class TokenAuth(BaseAuthentication):
    """自定义验证类"""

    def authenticate(self, request):
        """验证逻辑"""
        token = request._request.GET.get('token', '')
        print('token>>>>>>>',token)
        token_obj = Token.objects.filter(token=token).first()

        # 验证失败
        if not token_obj:
            raise AuthenticationFailed('认证失败')

        # 通过验证
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass


