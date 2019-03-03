# -*- coding: utf-8 -*-
from model.contact import Info


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Info(firstname="qwerty", lastname="eeeeeeeeee")
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)


# app.contact.create(Info(firstname="qwerty", middlename="aaaaaaaa", lastname="eeeeeeeeee", nick="rrrrrrrrr", title="aaaaaaaaa",cname="ssssssssss", address="dddddddddddd", homedid="fffffffff", cellular="gggggggggg",workdid="hhhhhhhhh", fax="555555555", email="ppppppp", email2="ooooooo", email3="iiiiiiiiiiii", website="ffffffffffff", address2="ssssssssssssssssssssssssssssssssssssssssssss", home="555444333",notes="fffffffffffffffffffffffffffffffffffffffffff"))
