# -*- coding: utf-8 -*-
from model.contact import Info
import random
# from random import randrange



# def test_delete_some_group_db(app, db, check_ui):
#        if len(db.get_group_list()) == 0:
#               app.group.create(Group(groupname="test"))
#        old_groups = db.get_group_list()
#        group = random.choice(old_groups)
#        app.group.delete_group_by_id(group.id)
#        assert len(old_groups) - 1 == app.group.count()
#        new_groups = db.get_group_list()
#        old_groups.remove(group)
#        assert old_groups == new_groups
#        if check_ui:
#               assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_delete_contact_db(app, db, check_ui):
       if len(db.get_contact_list()) == 0:
              app.contact.create(Info(firstname="test"))
       old_contacts = db.get_contact_list()
       contact = random.choice(old_contacts)
       app.contact.delete_contact_by_id(contact.id)
       assert len(old_contacts) - 1 == app.contact.count()
       new_contacts = db.get_contact_list()
       old_contacts.remove(contact)
       assert old_contacts == new_contacts
       if check_ui:
              assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                        key=Info.id_or_max)

# def test_delete_contact(app):
#        if app.contact.count() == 0:
#               app.contact.create(Info(firstname="test"))
#        old_contacts = app.contact.get_contact_list()
#        index = randrange(len(old_contacts))
#        app.contact.delete_contact_by_index(index)
#        assert len(old_contacts) - 1 == app.contact.count()
#        new_contacts = app.contact.get_contact_list()
#        old_contacts[index:index+1] = []
#        assert old_contacts == new_contacts
