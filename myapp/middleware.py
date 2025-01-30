from django.urls import reverse
from django.shortcuts import redirect


class RedirectAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            path_to_redirects = [reverse("loginPage"),reverse("registerPage")]

            if request.path in path_to_redirects:
                return redirect(reverse("landingPage"))
    
        response = self.get_response(request)
        return response
    
class RestrictUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        restricted_path = [reverse('dashboardPage'),reverse('taskListPage')]

        if not request.user.is_authenticated and request.path in restricted_path:
            return redirect(reverse('loginPage'))
        
        response = self.get_response(request)
        return response
