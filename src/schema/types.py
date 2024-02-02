from ariadne import make_executable_schema, load_schema_from_path,snake_case_fallback_resolvers,ObjectType, QueryType
from .resolvers import resolve_employee, resolve_department, resolve_department_employees, resolve_department_parent, resolve_employee_department, myfunc
from ariadne.validation import cost_directive

query = QueryType()
query.set_field("listEmployees",resolve_department)
query.set_field("employeeInfo",resolve_employee)
query.set_field("employee", resolve_employee)
query.set_field("department", resolve_department)

employee= ObjectType('Employee')
employee.set_field("relatesTo", myfunc)

department= ObjectType('Department')
department.set_field("relatesTo", myfunc)

employee_relation = ObjectType('EmployeeRelation')
employee_relation.set_field('department', resolve_employee_department)

department_relation = ObjectType('DepartmentRelation')
department_relation.set_field("employees", resolve_department_employees)
department_relation.set_field("parentDepartment", resolve_department_parent)
type_defs = load_schema_from_path("src/graphql/schema.graphql")


schema = make_executable_schema([type_defs, cost_directive],query,employee, department, employee_relation, department_relation,snake_case_fallback_resolvers) 
