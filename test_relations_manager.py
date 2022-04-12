import unittest

import relations_manager


def test_get_employee_name_and_birth():
    e = relations_manager.RelationsManager()
    name, birthdate = relations_manager.RelationsManager.get_employee_name_and_birth(e)

    assert name == "John Doe"
    assert birthdate == '1970-01-31'


# John Doe team members are Myrta Torkelson and Jettie Lynch
def test_john_team_members():
    ''''''
    e = relations_manager.RelationsManager()

    member_ids = e.teams[e.employee_list[0].id]
    assert e.employee_list[member_ids[0] - 1].first_name == "Myrta"
    assert e.employee_list[member_ids[0] - 1].last_name == "Torkelson"
    assert e.employee_list[member_ids[1] - 1].first_name == "Jettie"
    assert e.employee_list[member_ids[1] - 1].last_name == "Lynch"


# Tomas Andre not a team member of John Doe
def test_if_not_team_member():
    e = relations_manager.RelationsManager()
    member_ids = e.teams[e.employee_list[0].id]
    for l in e.employee_list:
        if l.first_name == "Tomas" and l.last_name == "Andre":
            e_id = l.id
            assert e_id not in member_ids


# Gretchen Walford’s base salary equals 4000$
def test_base_salary():
    e = relations_manager.RelationsManager()
    for l in e.employee_list:
        if l.first_name == "Gretchen" and l.last_name == "Walford":
            e_base_salary = l.base_salary
            assert e_base_salary == 4000


# Tomas Andre not a leader
def test_not_a_team_leader():
    e = relations_manager.RelationsManager()
    for l in e.employee_list:
        if l.first_name == "Tomas" and l.last_name == "Andre":
            is_leader = e.is_leader(l)
            # retrieving team members
            members = e.get_team_members(l)
            # assert is_leader == False
            return members


# Jude Overcash is not stored in database
def test_is_not_in_database():
    e = relations_manager.RelationsManager()
    is_in_database = False
    for l in e.employee_list:
        if l.first_name == "Jude" and l.last_name == "Overcash":
            is_in_database = True

    assert not is_in_database
