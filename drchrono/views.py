from django.shortcuts import redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth

from drchrono.endpoints import DoctorEndpoint, PatientEndpoint, \
    AppointmentProfileEndpoint


class SetupView(TemplateView):
    """
    The beginning of the OAuth sign-in flow. Logs a user into the kiosk, and saves the token.
    """
    template_name = 'kiosk_setup.html'


class DoctorWelcome(TemplateView):
    """
    The doctor can see what appointments they have today.
    """
    template_name = 'doctor_welcome.html'

    def get_token(self):
        """
        Social Auth module is configured to store our access tokens. This dark magic will fetch it for us if we've
        already signed in.
        """
        oauth_provider = UserSocialAuth.objects.get(provider='Chronos')
        access_token = oauth_provider.extra_data['access_token']
        return access_token

    def make_api_request(self):
        """
        Use the token we have stored in the DB to make an API request and get doctor details. If this succeeds, we've
        proved that the OAuth setup is working
        """
        # We can create an instance of an endpoint resource class, and use it to fetch details
        access_token = self.get_token()
        api = DoctorEndpoint(access_token)
        # Grab the first doctor from the list; normally this would be the whole practice group, but your hackathon
        # account probably only has one doctor in it.
        return api.list()

    def make_api_request_to_patients(self):
        """
        Use the token we have stored in the DB to make an API request and get doctor details. If this succeeds, we've
        proved that the OAuth setup is working
        """
        # We can create an instance of an endpoint resource class, and use it to fetch details
        access_token = self.get_token()
        api = PatientEndpoint(access_token)
        # print(api, 'response')
        # print(api.__dict__)
        # Grab the first doctor from the list; normally this would be the whole practice group, but your hackathon
        # account probably only has one doctor in it.

        return api.list()

    def make_api_request_to_appointment_profiles(self):
        access_token = self.get_token()
        api = AppointmentProfileEndpoint(access_token)
        return api.list()

    def get_context_data(self, **kwargs):
        kwargs = super(DoctorWelcome, self).get_context_data(**kwargs)
        # Hit the API using one of the endpoints just to prove that we can
        # If this works, then your oAuth setup is working correctly.
        # doctor_details = self.make_api_request()
        # kwargs['doctor'] = doctor_details
        # patients_details = self.make_api_request_to_patients()
        #
        # kwargs['patients'] = patients_details
        # appointment_profile_details = \
            # self.make_api_request_to_appointment_profiles()
        # kwargs['appointment_profiles'] = appointment_profile_details
        # for patient_detail in patients_details:
        #     print(patient_detail)
        return kwargs

