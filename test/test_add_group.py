from model.data import Group



def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="Group 01", group_footer="Group 01 footer")
    app.group.add(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
