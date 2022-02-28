import unittest

import relations_manager


def test_get_employee_name_and_birth():
    e = relations_manager.RelationsManager()
    name, birthdate = relations_manager.RelationsManager.get_employee_name_and_birth(e)

    assert name == "John Doe"
    assert birthdate == '1970-01-31'

