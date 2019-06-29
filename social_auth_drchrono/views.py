import hashlib
import hmac
import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name="dispatch")
class WebHookApi(View):

    def get(self, request):
        print(request.GET)
        response = self.webhook_verify(request)
        print(response)
        return JsonResponse(response)
        
    def post(self, request, *args, **kwargs):
        signature = request.META.get('HTTP_X_DRCHRONO_SIGNATURE')
        if signature == "unodostres456":
            event = request.META.get('HTTP_X_DRCHRONO_EVENT')
            print(request.body.decode('utf-8'))
            body_request = request.body.decode('utf-8')
            try:
                receiver = body_request.get('receiver')
                _object = body_request.get('object')
            except AttributeError as e:
                # If _object doesn't exist when the event is diferent to ping, 
                # we need save version object without with warning or it doesn't save 
                print(e)
            print(receiver)
            print(_object)
            if event == "PING":
                response = {}
            elif event == "APPOINTMENT_CREATE":
                pass
            elif event == "APPOINTMENT_MODIFY":
                pass
            elif event == "PATIENT_CREATE":
                pass
            elif event == "PATIENT_MODIFY":
                pass
            elif event == "PATIENT_PROBLEM_CREATE":
                pass
            elif event == "PATIENT_PROBLEM_MODIFY":
                pass
            elif event == "PATIENT_ALLERGY_CREATE":
                pass
            elif event == "PATIENT_ALLERGY_MODIFY":
                pass
            elif event == "PATIENT_MEDICATION_CREATE":
                pass
            elif event == "PATIENT_MEDICATION_MODIFY":
                pass
            elif event == "CLINICAL_NOTE_LOCK":
                pass
            elif event == "CLINICAL_NOTE_UNLOCK":
                pass
            
            return JsonResponse(response)
        else:
            response = {}
            return JsonResponse(status=403, data=response)

    def webhook_verify(self, request):
        try:
            token = 'unodostres456'.encode(encoding='utf-8')
            message = request.GET['msg'].encode(encoding='utf-8')
            secret_token = hmac.new(token, message,
                                    hashlib.sha256).hexdigest()
        except MultiValueDictKeyError as e:
            print(e)
            secret_token = None
        return {
            'secret_token': secret_token
        }

