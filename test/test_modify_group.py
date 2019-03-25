# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random

# if len(db.get_group_list()) == 0:
#         app.group.create(Group(groupname="test"))
# old_groups = db.get_group_list()
# group = random.choice(old_groups)
# app.group.delete_group_by_id(group.id)
# assert len(old_groups) - 1 == app.group.count()
# new_groups = db.get_group_list()
# old_groups.remove(group)
# assert old_groups == new_groups


def test_modify_group_name_db(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(groupname="test"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        changed_group = Group(groupname="Group2")
        changed_group.id = group.id
        app.group.modify_group_by_id(group.id, changed_group)
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups.remove(group)
        old_groups.append(changed_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_name(app):
#         if app.group.count() == 0:
#                 app.group.create(Group(groupname="test"))
#         old_groups = app.group.get_group_list()
#         index = randrange(len(old_groups))
#         group = Group(groupname="Group2")
#         group.id = old_groups[index].id
#         app.group.modify_group_by_index(index, group)
#         assert len(old_groups) == app.group.count()
#         new_groups = app.group.get_group_list()
#         old_groups[index] = group
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#        if app.group.count() == 0:
#                app.group.create(Group(groupname="test"))
#        old_groups = app.group.get_group_list()
#        app.group.modify_first_group(Group(header="bbbbbbbb"))
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)


