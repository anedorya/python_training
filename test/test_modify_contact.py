# -*- coding: utf-8 -*-
from model.contact import Info

# def test_modify_contact(app):
#        if app.contact.count() == 0:
#                app.contact.create(Info(firstname="test"))
#        app.contact.modify(Info(firstname="ssssss"))


def test_modify_contact(app):
        if app.contact.count() == 0:
                app.contact.create(Info(firstname="test"))
        old_contacts = app.contact.get_contact_list()
        contact = Info(firstname="fffffff", lastname="ddddddd")
        contact.id = old_contacts[0].id
        app.contact.modify(contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[0] = contact
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)




#       app.contact.modify(Info(firstname="qqq", middlename="www", lastname="eee", nick="ttt", title="rrr", cname="yyy", address="yyy", homedid="111", cellular="222", workdid="333", fax="444", email="kkk", email2="aaa", email3="sss", website="ddd", address2="fff", home="666", notes="zzz"))