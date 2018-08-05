from model.data import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Hank", lastname="Hill", address="Texas"))
    app.contact.delete()
