from model.data import Group
from random import randrange


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.add(Group("Group 02", "Group 02 footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="Modified")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
