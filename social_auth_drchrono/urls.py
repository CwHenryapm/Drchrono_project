from django.conf.urls import url


from social_auth_drchrono.views import VerifyWebHookView

urlpatterns = [
    url(r'^webhooks/verify/$', VerifyWebHookView.as_view(),
        name='verify_webhooks'),
]