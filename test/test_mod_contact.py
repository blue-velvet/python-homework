from model.data import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Hank", lastname="Hill", address="Texas"))
    app.contact.modify(Contact(firstname="Anna", lastname="Frank"))
