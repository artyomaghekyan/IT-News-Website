from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.

def home(request):
    q = request.GET.get('q')
    try:
        news = News.objects.filter(title__icontains=q)
    except ValueError:
        news = News.objects.all()
    
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    
    context = {'news': news, 'page_obj': page_obj}
    return render(request, 'base/home.html', context)

class DetailNews(DetailView):
    model = News
    template_name = 'base/detail.html'
    context_object_name = 'detail'

class UploadNews(CreateView):
    action = 'create'
    model = News
    form_class = NewsForm
    template_name = 'base/crud.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = self.action
        return context

    def form_valid(self, form):
        # Save the form and associated image to the database
        self.object = form.save(commit=False)
        self.object.image = form.cleaned_data['image']
        self.object.save()
        return super().form_valid(form)

class EditNews(UpdateView):
    model = News
    action = 'edit'
    template_name = 'base/crud.html'
    form_class = NewsForm
    success_url = reverse_lazy('home')
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = self.action
        return context

    def form_valid(self, form):
        # Set the author of the News instance to the current user
        form.instance.author = self.request.user

        # Call the parent form_valid method to save the form data
        return super().form_valid(form)

class DeleteNews(DeleteView):
    action = 'delete'
    model = News
    template_name = 'base/crud.html'
    success_url = reverse_lazy('home')
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = self.action
        return context
    






