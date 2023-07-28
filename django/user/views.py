from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import CustomUser
from .forms import CustomUserForm


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'user/user_detail.html'
    context_object_name = 'user'


class CreateUserView(CreateView):
    model = CustomUser
    template_name = 'user/create_user.html'
    fields = ['username', 'email']

    def get(self, request):
        form = CustomUserForm()
        return render(request, 'user/create_user.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user/create_user.html', {'form': form})


# def create_users(request):
#     # Створюємо список користувачів для заповнення таблиці
#     users_to_create = [
#         CustomUser(username='John', email='john@example.com'),
#         CustomUser(username='Alice', email='alice@example.com'),
#         CustomUser(username='Bob', email='bob@example.com'),
#         CustomUser(username='Mary', email='mary@example.com'),
#         CustomUser(username='Michael', email='michael@example.com'),
#         CustomUser(username='Emma', email='emma@example.com'),
#         CustomUser(username='David', email='david@example.com'),
#         CustomUser(username='Olivia', email='olivia@example.com'),
#         CustomUser(username='William', email='william@example.com'),
#         CustomUser(username='Sophia', email='sophia@example.com'),
#     ]
#
#     CustomUser.objects.bulk_create(users_to_create)
#
#     return JsonResponse("Дані про користувачів були додані до бази даних.")
