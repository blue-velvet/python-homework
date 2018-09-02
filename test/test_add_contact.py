from model.data import Contact
from random import randint


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    phone_num = randint[10000:99999]
    contact = Contact(firstname="John", lastname="Doe", address="Baker str.", homephone=str(phone_num),
                      mobilephone=str(phone_num), workphone=str(phone_num), secondaryphone=str(phone_num))
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
