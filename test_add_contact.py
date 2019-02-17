# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Info

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.add_contact(Info(firstname="qwerty", middlename="aaaaaaaa", lastname="eeeeeeeeee", nick="rrrrrrrrr", title="aaaaaaaaa", cname="ssssssssss", address="dddddddddddd", homedid="fffffffff", cellular="gggggggggg", workdid="hhhhhhhhh", fax="555555555", email="ppppppp", email2="ooooooo",email3="iiiiiiiiiiii", website="ffffffffffff",address2="ssssssssssssssssssssssssssssssssssssssssssss", home="555444333", notes="fffffffffffffffffffffffffffffffffffffffffff", byear="1980", ayear="2000"))
        app.logout()
