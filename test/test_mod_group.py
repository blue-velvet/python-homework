from model.data import Group


def test_add_group(app):
    app.session.login()
    app.group.modify(Group("Modified", "Modified"))
    app.session.logout()
