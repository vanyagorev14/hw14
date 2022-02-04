from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from polls.tasks import celery_send_mail
from .forms import Reminder
from django.views import generic
from .forms import CommentForm
from .models import Comment, Post
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, get_user_model, login

User = get_user_model()

def reminder(request):
    if request.method == "POST":
        form = Reminder(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['email']
            time = form.cleaned_data['time']
            celery_send_mail.apply_async((message, receiver), eta=time)
            messages.success(request, 'Remind is created')
            return redirect('')
        else:
            messages.error(request, 'Reminder not created!')
    else:
        form = Reminder()

    return render(request, "index.html", context={"form": form})


class PostList(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'bloging/listing.html'

    def get_queryset(self):
        return Post.objects.all().filter(posted=True)


def post_det(request, pk):
    post = get_object_or_404(Post, pk=pk, posted=True)
    comments = Comment.objects.all().filter(post=post)
    paginator = Paginator(comments, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comn = Comment
            comn.username = form.cleaned_data['username']
            comn.text = form.cleaned_data['text']
            comn.post = post
            comn.save()
            return HttpResponseRedirect(reverse('detailing', args=(post.id,)))
    else:
        initial = {'username': request.user.username}
        form = CommentForm(initial=initial)

    context = {'form': form, 'post': post, 'page_obj': page_obj}
    return render(request, 'bloging/detailing.html')


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user).filter(posted=True)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    paginator = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'obj': user,
    }
    return render(request, 'bloging/user.html')