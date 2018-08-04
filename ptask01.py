import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Group, Contact
from application import Application


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









