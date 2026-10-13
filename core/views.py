from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, StudentForm
from .models import Student


@login_required
def dashboard(request):
    students = Student.objects.filter(created_by=request.user)
    context = {
        "total_students": students.count(),
        "active_courses": students.values("course").distinct().count(),
        "average_age": round(students.aggregate(avg=Avg("age"))["avg"] or 0, 1),
        "recent_students": students[:5],
    }
    return render(request, "core/dashboard.html", context)


@login_required
def student_list(request):
    students = Student.objects.filter(created_by=request.user)
    query = request.GET.get("q", "").strip()
    course = request.GET.get("course", "").strip()

    if query:
        students = students.filter(
            Q(full_name__icontains=query)
            | Q(email__icontains=query)
            | Q(mobile__icontains=query)
        )
    if course:
        students = students.filter(course=course)

    paginator = Paginator(students, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "core/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
            "query": query,
            "selected_course": course,
            "courses": Student.COURSE_CHOICES,
        },
    )


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            messages.success(request, "Student registered successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(
        request,
        "core/student_form.html",
        {"form": form, "title": "Register New Student", "button": "Save Student"},
    )


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "core/student_form.html",
        {"form": form, "title": "Edit Student", "button": "Update Student"},
    )


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, created_by=request.user)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")

    return redirect("student_list")


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form": form})
