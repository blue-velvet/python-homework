from model.data import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Hank", lastname="Hill", address="Texas"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
