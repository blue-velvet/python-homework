from model.data import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.add(Group("Group 02", "Group 02 footer"))
    app.group.modify(Group(group_name="Modified"))
