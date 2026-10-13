from django.db import models


class Student(models.Model):
    COURSE_CHOICES = [
        ("Computer Science", "Computer Science"),
        ("Data Science", "Data Science"),
        ("UI/UX Design", "UI/UX Design"),
        ("Business Administration", "Business Administration"),
        ("Python Fullstack","Python Fullstack"),
        ("Java Fullstack","Java Fullstack"),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    course = models.CharField(max_length=80, choices=COURSE_CHOICES)
    age = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="students",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name
