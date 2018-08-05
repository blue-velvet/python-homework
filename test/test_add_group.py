from model.data import Group


def test_add_group(app):
    app.group.add(Group("Group 01", "Group 01 footer"))
