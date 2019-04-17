# -*- coding: utf-8 -*-
from model.group import Group
import pytest



def test_add_group_db(app, db, check_ui, json_groups):
        group = json_groups
        old_groups = db.get_group_list()
        app.group.create(group)
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_add_group(app, json_groups):
#         group = json_groups
#         old_groups = app.group.get_group_list()
#         app.group.create(group)
#         assert len(old_groups) + 1 == app.group.count()
#         new_groups = app.group.get_group_list()
#         old_groups.append(group)
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#         #               app.session.logout()



# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, group):
#         old_groups = app.group.get_group_list()
#         app.group.create(group)
#         assert len(old_groups) + 1 == app.group.count()
#         new_groups = app.group.get_group_list()
#         old_groups.append(group)
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#         #               app.session.logout()