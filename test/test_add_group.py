# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
        app.group.create(Group(groupname="Group1", header="asdasdasda", footer="aaaaaaa"))

def test_add_empty_group(app):
        app.group.create(Group(groupname="", header="", footer=""))


