from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from account.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
class CreateInstaPostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'login_register.html'
    fields = ['media', 'caption']
    success_url = '/login'

    def form_valid(self, form):
        user = self.request.user
        profile = UserProfile.objects.get(owner=user)
        form.instance.profile = profile
        super().form_valid(form)
        return HttpResponse('Post is created')

    def form_invalid(self, form):
        super().form_invalid(form)
        return HttpResponse('Unsuccessful!!')


@login_required(login_url='login')
def updateInstaPost(request):
    user = request.user
    pr = UserProfile.objects.get(owner=user)
    for i in Post.objects.filter(profile=pr):
        print(i.pk)
    # profile = user.userprofile_set.get(owner=user)
    # print(profile, '=========')
    # post = profile.post_set.get(id=pk)
    return HttpResponse('Successful!!')
