import pytest

from fixture.application import Application
from model.data import Group, Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login()
    app.add_group(Group("Group 01", "Group 01 footer"))
    app.logout()


def test_add_contact(app):
    app.login()
    app.add_contact(Contact("John", "Doe", "Baker str."))
    app.logout()









