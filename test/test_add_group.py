from model.data import Group


def test_add_group(app):
    app.group.add(Group(group_name="Group 01", group_footer="Group 01 footer"))
