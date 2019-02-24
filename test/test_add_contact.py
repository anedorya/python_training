# -*- coding: utf-8 -*-
from model.contact import Info


def test_add_contact(app):
        app.contact.create(Info(firstname="qwerty", middlename="aaaaaaaa", lastname="eeeeeeeeee", nick="rrrrrrrrr", title="aaaaaaaaa", cname="ssssssssss", address="dddddddddddd", homedid="fffffffff", cellular="gggggggggg", workdid="hhhhhhhhh", fax="555555555", email="ppppppp", email2="ooooooo", email3="iiiiiiiiiiii", website="ffffffffffff", address2="ssssssssssssssssssssssssssssssssssssssssssss", home="555444333", notes="fffffffffffffffffffffffffffffffffffffffffff"))
