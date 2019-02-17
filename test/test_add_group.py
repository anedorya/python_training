# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(groupname="Group1", header="asdasdasda", footer="aaaaaaa"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(groupname="", header="", footer=""))
        app.session.logout()


