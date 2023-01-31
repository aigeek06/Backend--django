# Backend-django

# Problem
In this assignment you have to implement google calendar integration using django rest api. You need to use the OAuth2 mechanism toget users calendar access. 
Below are detail of API endpoint and corresponding views which you need to implement

/rest/v1/calendar/init/ -> GoogleCalendarInitView()
This view should start step 1 of the OAuth. Which will prompt user for his/her credentials
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()

This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar

# Solution
1. First, create the GoogleCalendarInitView class-based view in Django for handling the initial step of the OAuth2 mechanism. This view will redirect the user to the Google authorization page where the user can grant access to the calendar.

2. In the GoogleCalendarRedirectView, implement the code to handle the redirect request sent by Google with the authorization code. Use this code to make a request to the Google API to obtain the access token.

3. Once you have the access token, use it to make a request to the Google Calendar API to retrieve the list of events in the user's calendar.

4. Return the list of events as a JSON response. You can use the Django Rest Framework for creating and returning the JSON response.

5. Make sure to properly handle exceptions and errors that may occur during the implementation process.

6. You can use the Google API Client library provided by Google for interacting with the Google Calendar API.
