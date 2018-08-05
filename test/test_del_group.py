def test_delete_group(app):
    app.session.login()
    app.group.delete()
    app.session.logout()
