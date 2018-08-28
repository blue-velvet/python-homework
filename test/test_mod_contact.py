from model.data import Contact
from random import randrange


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Hank", lastname="Hill", address="Texas"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Anna", lastname="Frank")
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(contact, index)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
