from model.data import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.add(Group("Group 02", "Group 02 footer"))
    app.group.delete()
