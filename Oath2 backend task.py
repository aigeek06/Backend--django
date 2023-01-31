from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import requests

class GoogleCalendarInitView(View):
    def get(self, request, *args, **kwargs):
        # Generate the OAuth2 authorization URL
        authorization_url, state = self.get_authorization_url()
        # Save the state in the session
        request.session['oauth_state'] = state
        # Redirect the user to the authorization URL
        return redirect(authorization_url)

    def get_authorization_url(self):
        # Replace with your own client ID and secret
        client_id = "YOUR_CLIENT_ID"
        client_secret = "YOUR_CLIENT_SECRET"
        redirect_uri = "http://localhost:8000/rest/v1/calendar/redirect/"

        # Request an authorization code
        authorization_url = f"https://accounts.google.com/o/oauth2/v2/auth?" \
                            f"response_type=code&" \
                            f"client_id={client_id}&" \
                            f"redirect_uri={redirect_uri}&" \
                            f"scope=https://www.googleapis.com/auth/calendar&" \
                            f"access_type=offline&" \
                            f"prompt=consent"

        # Generate a state token to prevent request forgery
        state = "random_state_token"

        return authorization_url, state

class GoogleCalendarRedirectView(View):
    def get(self, request, *args, **kwargs):
        # Check if the state token is valid
        if request.GET.get('state') != request.session['oauth_state']:
            return redirect(reverse('error'))

        # Get the authorization code
        code = request.GET.get('code')
        if not code:
            return redirect(reverse('error'))

        # Use the authorization code to get the access token
        access_token = self.get_access_token(code)
        if not access_token:
            return redirect(reverse('error'))

        # Use the access token to get the list of events
        events = self.get_events(access_token)
        if not events:
            return redirect(reverse('error'))

        # Return the list of events as a JSON response
        return JsonResponse(events, safe=False)

    def get_access_token(self, code):
        # Replace with your own client ID and secret
        client_id = "YOUR_CLIENT_ID"
        client_secret = "YOUR_CLIENT_SECRET"
        redirect_uri = "http://localhost:8000/rest/v1/calendar/redirect/"

        # Request an access token
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": client_id,
        }