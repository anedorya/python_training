# -*- coding: utf-8 -*-
from model.contact import Info
import pytest



def test_add_contact(app, json_contacts):
        contact = json_contacts
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)



# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_add_contact(app, contact):
#         old_contacts = app.contact.get_contact_list()
#         app.contact.create(contact)
#         assert len(old_contacts) + 1 == app.contact.count()
#         new_contacts = app.contact.get_contact_list()
#         old_contacts.append(contact)
#         assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)
