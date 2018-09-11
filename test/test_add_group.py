from model.data import Group
import time


def test_add_group(app, db, json_group):
    group = json_group
    old_groups = db.get_group_list()
    app.group.add(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
