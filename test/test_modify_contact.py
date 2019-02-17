# -*- coding: utf-8 -*-
from model.contact import Info


def test_modify_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify(Info(firstname="qqq", middlename="www", lastname="eee", nick="ttt", title="rrr", cname="yyy", address="yyy", homedid="111", cellular="222", workdid="333", fax="444", email="kkk", email2="aaa", email3="sss", website="ddd", address2="fff", home="666", notes="zzz", byear="1900", ayear="1950"))
        app.session.logout()
