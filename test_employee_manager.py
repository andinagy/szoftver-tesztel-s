
import datetime
import employee_manager

# Check an employee’s salary who is not a team leader whose hire date is 10.10.1998 and his base salary is 1000$.
# Make sure the returned value is 3000$ (1000$ + 20 X 100$).
import relations_manager

def test_check_salary():
    rm = relations_manager.RelationsManager()
    e = employee_manager.EmployeeManager(rm)
    e_list = rm.employee_list
    salary = 0
    for l in e_list:
        if l.hire_date == datetime.date(1998, 10, 10) and l.base_salary == 1000 and rm.is_leader(l) == False:
            salary = e.calculate_salary(l)
            assert salary == 3000

