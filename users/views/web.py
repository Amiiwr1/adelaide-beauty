from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "users/signup.html"


class SignInView(TemplateView):
    template_name = "users/login.html"
