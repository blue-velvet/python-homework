from model.data import Contact


def test_mod_contact(app):
    app.contact.modify(Contact(firstname="Anna", lastname="Frank"))
