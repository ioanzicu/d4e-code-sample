from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed, Cat
from cats.forms import BreedForm


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        all_cats = Cat.objects.all()

        context = {'breed_count': breed_count, 'cat_list': all_cats}
        return render(request, 'cats/cat_list.html', context)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_all = Breed.objects.all()
        context = {'breed_list': breed_all}
        return render(request, 'cats/breed_list.html', context)


class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = BreedForm()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)

        breed = form.save()
        return redirect(self.success_url)


class BreedUpdate(LoginRequiredMixin, View):
    breed = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.breed, pk=pk)
        form = BreedForm(instance=breed)
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request, pk):
        breed = get_object_or_404(self.breed, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)

        form.save()
        return redirect(self.success_url)


class BreedDelete(LoginRequiredMixin, View):
    breed = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.breed, pk=pk)
        form = BreedForm(instance=breed)
        context = {'breed': breed}
        return render(request, self.template, context)

    def post(self, request, pk):
        breed = get_object_or_404(self.breed, pk=pk)
        breed.delete()
        return redirect(self.success_url)


class CatCreate(LoginRequiredMixin, CreateView):
    cat = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
    template_name = 'cats/cat_form.html'

    def get_queryset(self):
        return Cat.objects.all()


class CatUpdate(LoginRequiredMixin, UpdateView):
    cat = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

    def get_queryset(self):
        return Cat.objects.all()


class CatDelete(LoginRequiredMixin, DeleteView):
    cat = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

    def get_queryset(self):
        return Cat.objects.all()
