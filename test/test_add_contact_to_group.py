# -*- coding: utf-8 -*-
from model.contact import Info
from model.group import Group
import pytest
import random
from fixture.orm import ORMfixture


def test_add_contact_to_group_db(app, db, check_ui):
        db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")
        if len(db.get_contact_list()) == 0:
                app.contact.create(Info(firstname="test"))
        if len(db.get_group_list()) == 0:
                app.group.create(Group(groupname="test"))
        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
        new_contacts_in_group_from_db = db.get_contacts_in_group(Group(id=group.id))
        new_contacts_in_group_from_ui = app.contact.get_list_of_contacts_in_group_by_id(group.id)
        assert sorted(new_contacts_in_group_from_db, key=Info.id_or_max) == sorted(new_contacts_in_group_from_ui,
                                                                  key=Info.id_or_max)

        # contact = json_contacts
        # old_contacts = db.get_contact_list()
        # app.contact.create(contact)
        # new_contacts = db.get_contact_list()
        # old_contacts.append(contact)
        # assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)
        # if check_ui:
        #         assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(),
        #                                                                   key=Info.id_or_max)


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