# -*- coding: utf-8 -*-
from model.contact import Info
import pytest
import random
import string

def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Info(firstname="", middlename="", lastname="")] + [
#         Info(firstname=random_string("FN", 10), middlename=random_string("MN", 10), lastname=random_string("LN", 10),
#              address=random_string("ADDRESS", 10), homedid=random_string("HOME", 10))
#         for i in range(5)
# ]

testdata = [
        Info(firstname=firstname, middlename=middlename, lastname=lastname)
        for firstname in ["", random_string("FN", 10)]
        for middlename in ["", random_string("MN", 20)]
        for lastname in ["", random_string("LN", 20)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(old_contacts, key=Info.id_or_max)
