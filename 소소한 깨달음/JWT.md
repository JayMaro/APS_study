csrf token은 JWT에서 필요 없는건가?



JWT에는 두가지 토큰이 있다.

ACCESS - 만료 시간이 짧다. -> 만료되면 REFRESH 토큰을 보낸다. -> 다시 새로운 ACCESS 토큰을 발급 받는다. 

REFRESH - 만료 시간이 길다.



순서대로 되어야 한다.

like view함수 위에 작성되는 middleware



올바른 method로 요청했는지 확인

@api_view(['GET', 'POST'])



JWT값이 유효한지 파악(인증이 유효한지 파악)

@authentication_classes([JSONWebTokenAuthentication])



인증상태에서만 통과

@permission_classes([IsAuthenticated])





```
settings.py에 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
이게 있다면 위의 항목들이 모든 views 함수에 대해 데코레이터를 추가하는 효과와 동일하다
```





https://router.vuejs.org/kr/guide/advanced/navigation-guards.html



```
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
```