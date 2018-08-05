from model.data import Contact


def test_mod_contact(app):
    app.session.login()
    app.contact.modify(Contact(firstname="Anna", lastname="Frank"))
    app.session.logout()
