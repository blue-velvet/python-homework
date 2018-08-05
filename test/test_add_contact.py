from model.data import Contact


def test_add_contact(app):
    app.contact.add(Contact(firstname="John", lastname="Doe", address="Baker str."))
