from .forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def instagram_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        print(request.POST, '===================')
        if form.is_valid():
            # datas = form.cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, "Username does not exist!")
            user = authenticate(username=username, password=password)
            print(user, '===========================')
            if user:
                login(request, user)
                print('Ok+++++++++++++++++++++++++')
                return HttpResponse('User logged in!')

            else:
                # messages.error(request, "Username or password incorrect!")
                return HttpResponse('Username or password incorrect!!')
        else:
            print("Form invalid")
    form = LoginForm()
    return render(request, 'login_register.html', {'form': form})

# class InstagramSignUpView(View):
#     http_method_names = ['get', 'post']
#     template_name = 'login_register.html'
#     form_class = SignUpForm
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         if request.FILES:
#             files = request.FILE
#         else:
#             files = None
#         form = self.form_class(request.POST, files)
#         if form.is_valid():
#             user = form.save()
#             bio = form.cleaned_data['bio']
#             profile_pic = form.cleaned_data['profile_pic']
#             profile = UserProfile.objects.create(user=user, bio=bio,
#                                                  profile_pic=profile_pic)
#             profile.save()
#             return HttpResponse('User registration successful!!')
#         else:
#             return HttpResponse('Registration failed!!')
#
#
# class CreatePostView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post_creation.html'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
