from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from blog.forms import *
from django.db import IntegrityError
from blog.models import *
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
class Index(ListView):
    paginate_by = 2
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        paginator = Paginator(Blog.objects.all(), 3)
        return context


class CreateBlog(CreateView):
    form_class = CreatePersonalBlogForm
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create blog'
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PersonalBlogs(ListView):
    paginate_by = 2
    model = Blog
    template_name = 'blog/personal_blogs.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    pk_url_kwarg = 'blog_id'
    def get_queryset(self):
        return Blog.objects.filter(id=self.kwargs['blog_id'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Detail blog'
        context['blog'] = self.get_queryset()[0]
        return context




def modified_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, user=request.user)
    if request.method == 'GET':
        form = CreatePersonalBlogForm(instance=blog)
        dct = {'title': 'Modified blog information', 'form': form, 'blog': blog}
        return render(request, 'blog/modified_blog.html', context=dct)
    else:
        form = CreatePersonalBlogForm(request.POST, request.FILES, instance=blog)
        form.save()
        return redirect('home')
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, user=request.user)
    blog.delete()
    return redirect('home')
def sign_up_user(request):
    if request.method == 'GET':
        dct = {'title': 'Sign up', 'form': SignUpForm()}
        return render(request, 'blog/sign_up_user.html', context=dct)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                dct = {'title': 'Sign up', 'form': SignUpForm(), 'error': 'This username has already been taken! Maybe you should login...'}
                return render(request, 'blog/sign_up_user.html', context=dct)
        else:
            dct = {'title': 'Sign up', 'form': SignUpForm(), 'error': 'Your passwords are not match!'}
            return render(request, 'blog/sign_up_user.html', context=dct)
def login_user(request):
    if request.method == 'GET':
        dct = {'title': 'Login', 'form': LoginUserForm()}
        return render(request, 'blog/login_user.html', context=dct)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            dct = {'title': 'Login', 'form': LoginUserForm(), 'error': 'Incorrect username or password!'}
            return render(request, 'blog/login_user.html', context=dct)
        else:
            login(request, user)
            return redirect('home')
def logout_user(request):
    logout(request)
    return redirect('home')