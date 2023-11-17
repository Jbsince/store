from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=250)
    wikipedia_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Purpose(models.Model):
    purpose = models.CharField(max_length=250)

    def __str__(self):
        return self.purpose
