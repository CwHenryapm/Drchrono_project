from django.conf.urls import url


from social_auth_drchrono.views import WebHookApi

urlpatterns = [
    url(r'^webhooks/verify/$', WebHookApi.as_view(),
        name='verify_webhooks'),
]