from model.data import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.add(Group(group_name="Group 01", group_footer="Group 01 footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
