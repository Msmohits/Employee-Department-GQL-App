from case_changer import snake_case


departments = [
    {
        "department_id": "1",
        "department_name": "Engineering",
        "parent_depatment_id": "3",
    },
    {"department_id": "2", "department_name": "Marketing", "parent_depatment_id": "5"},
    {"department_id": "3", "department_name": "Sales", "parent_depatment_id": "1"},
    {"department_id": "4", "department_name": "HR", "parent_depatment_id": "2"},
    {"department_id": "5", "department_name": "Admin", "parent_depatment_id": None},
]

employees = [
    {"employee_id": "1", "employee_name": "John Doe", "department_id": "1"},
    {"employee_id": "2", "employee_name": "Jane Smith", "department_id": "2"},
    {"employee_id": "3", "employee_name": "Jona Smith", "department_id": "1"},
    {"employee_id": "4", "employee_name": "Jerry Watson", "department_id": "3"},
    {"employee_id": "5", "employee_name": "Emma Watson", "department_id": "4"},
    {"employee_id": "6", "employee_name": "Sherry Boots", "department_id": "2"},
    {"employee_id": "7", "employee_name": "xyz abc", "department_id": "2"},
]


def resolve_employee(_, info, employeeId):
    employee = next(
        (employee for employee in employees if employee["employee_id"] == employeeId),
        None,
    )
    return employee


def resolve_department(_, info, departmentId):
    department = next(
        (
            department
            for department in departments
            if department["department_id"] == departmentId
        ),
        None,
    )
    return department


def resolve_employee_department(obj, info, *args, **kwargs):
    department = resolve_department(None, info, obj.get("department_id", ""))
    return department


def resolve_department_employees(obj, info, startWith=None, *args, **kwargs):
    return [
        employee
        for employee in employees
        if employee["department_id"] == obj.get("department_id", "")
        and (startWith is None or employee["employee_name"].startswith(startWith))
    ]


def resolve_department_parent(obj, info, *args, **kwargs):
    department = resolve_department(None, info, obj["parent_depatment_id"])
    return department

def myfunc(obj, info, *args, **kwargs):
    return obj

