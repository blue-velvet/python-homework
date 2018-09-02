from model.data import Contact
from random import randint
import pytest
import random
import string


def random_name(length):
    symbols = string.ascii_letters
    return "".join(random.choice(symbols) for i in range(random.randrange(length)))

def random_address(length):
    symbols = string.ascii_letters + string.digits + " "*10
    return "".join(random.choice(symbols) for i in range(random.randrange(length)))

def random_phone():
    return str(randint(10000, 99999))

testdata = [
    Contact(firstname=random_name(7), lastname=random_name(10), address=random_address(20), homephone=random_phone(),
                      mobilephone=random_phone(), workphone=random_phone(), secondaryphone=random_phone())
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
