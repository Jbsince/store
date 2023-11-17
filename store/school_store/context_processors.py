from .models import Department


def departments(request):
    # Fetch the departments from the database
    department_list = Department.objects.all()

    # Return a dictionary with the department list
    return {'department_list': department_list}
