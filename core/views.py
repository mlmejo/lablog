from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentForm
from .models import Student


def welcome(request):
    return render(request, "welcome.html", context={})


def home(request):
    return render(request, "home.html", context={})


def index(request):
    student_list = Student.objects.filter(disabled=False)
    return render(request, "index.html", context={"student_list": student_list})


def sign_in(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = StudentForm()

    return render(request, "sign-in.html", context={"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        form.save()
        return HttpResponseRedirect("/students")
    else:
        form = StudentForm(instance=student)
    return render(request, "edit.html", context={"form": form})


def delete_entry(request, pk):
    if request.method == "POST":
        student = Student.objects.get(pk=pk)
        student.disabled = True
        student.save()

        return HttpResponseRedirect("/students")


def retrieve_list(request):
    if request.method == "POST":
        for student in Student.objects.all():
            student.disabled = False
            student.save()

        return HttpResponseRedirect("/students")
