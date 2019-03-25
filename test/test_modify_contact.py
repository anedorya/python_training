# -*- coding: utf-8 -*-
from model.contact import Info
import random
from random import randrange


def test_modify_contact_db(app, db, check_ui):
        if len(db.get_contact_list()) == 0:
                app.contact.create(Info(firstname="test"))
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        changed_contact = Info(firstname="111qwerty", lastname="111eeeeeeeeee")
        app.contact.modify_contact_by_id(contact.id, changed_contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        old_contacts.append(changed_contact)
        assert sorted(old_contacts, key=Info.id_or_max) == sorted(new_contacts, key=Info.id_or_max)
        if check_ui:
                assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(), key=Info.id_or_max)


#
# def test_modify_contact(app):
#         if app.contact.count() == 0:
#                 app.contact.create(Info(firstname="test"))
#         old_contacts = app.contact.get_contact_list()
#         index = randrange(len(old_contacts))
#         contact = Info(firstname="111qwerty", lastname="111eeeeeeeeee")
#         contact.id = old_contacts[index].id
#         app.contact.modify_contact_by_index(index, contact)
#         assert len(old_contacts) == app.contact.count()
#         new_contacts = app.contact.get_contact_list()
#         old_contacts[index] = contact
#         assert sorted(old_contacts, key=Info.id_or_max) == sorted(new_contacts, key=Info.id_or_max)
#

#       app.contact.modify(Info(firstname="qqq", middlename="www", lastname="eee", nick="ttt", title="rrr", cname="yyy", address="yyy", homedid="111", cellular="222", workdid="333", fax="444", email="kkk", email2="aaa", email3="sss", website="ddd", address2="fff", home="666", notes="zzz"))