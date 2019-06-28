import hashlib
import hmac

from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View


class VerifyWebHookView(View):

    def get(self, request):
        print(request.GET)
        response = self.webhook_verify(request)
        print(response)
        return JsonResponse(response)

    def webhook_verify(self, request):
        try:
            secret_token = hmac.new('unodostres456', request.GET['msg'],
                                    hashlib.sha256).hexdigest()
        except MultiValueDictKeyError as e:
            print(e)
            secret_token = None
        return {
            'secret_token': secret_token
        }

