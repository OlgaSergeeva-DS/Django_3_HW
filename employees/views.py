from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import User


# Create your views here.
def home(request):
    # Берем всех сотрудников для главной
    employees = User.objects.all()[:3]  # Например, только 3 для главной
    return render(request, "home.html", {"employees": employees})


def employee_list(request):
    employees = User.objects.all()
    return render(request, "employees/employee_list.html", {"employees": employees})


@login_required  # <-- Это делает страницу доступной только авторизованным (К8)
def employee_detail(request, pk):
    employee = get_object_or_404(User, pk=pk)
    return render(request, "employees/employee_detail.html", {"employee": employee})
