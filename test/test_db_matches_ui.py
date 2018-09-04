from model.data import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def clean(group):
    return Group(id=group.id, group_name=group.group_name.strip(), group_footer=group.group_footer.strip())
