import pytest

from fixture.application import Application
from model.data import Group, Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login()
    app.group.add(Group("Group 01", "Group 01 footer"))
    app.session.logout()


def test_add_contact(app):
    app.session.login()
    app.contact.add(Contact("John", "Doe", "Baker str."))
    app.session.logout()
