from model.data import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.add(Group("Group 02", "Group 02 footer"))
    old_groups = app.group.get_group_list()
    group = Group(group_name="Modified")
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
