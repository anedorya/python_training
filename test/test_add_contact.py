# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Info

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Info(firstname="qwerty", middlename="aaaaaaaa", lastname="eeeeeeeeee", nick="rrrrrrrrr", title="aaaaaaaaa", cname="ssssssssss", address="dddddddddddd", homedid="fffffffff", cellular="gggggggggg", workdid="hhhhhhhhh", fax="555555555", email="ppppppp", email2="ooooooo", email3="iiiiiiiiiiii", website="ffffffffffff", address2="ssssssssssssssssssssssssssssssssssssssssssss", home="555444333", notes="fffffffffffffffffffffffffffffffffffffffffff", byear="1980", ayear="2000"))
        app.session.logout()
