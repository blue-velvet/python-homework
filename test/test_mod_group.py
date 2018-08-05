from model.data import Group


def test_mod_group(app):
    app.session.login()
    app.group.modify(Group(group_name="Modified"))
    app.session.logout()
