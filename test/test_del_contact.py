def test_delete_contact(app):
    app.session.login()
    app.contact.delete()
    app.session.logout()
