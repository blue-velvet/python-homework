from model.data import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="John", lastname="Doe", address="Baker str.")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
