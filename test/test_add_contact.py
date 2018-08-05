from model.data import Contact


def test_add_contact(app):
    app.session.login()
    app.contact.add(Contact("John", "Doe", "Baker str."))
    app.session.logout()
