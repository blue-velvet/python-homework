from model.data import Contact


def test_add_contact(app):
    app.session.login()
    app.contact.modify(Contact("Modified", "Modified", "Modified"))
    app.session.logout()
