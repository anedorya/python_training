# -*- coding: utf-8 -*-
from model.contact import Info

def test_delete_contact(app):
       if app.contact.count() == 0:
              app.contact.create(Info(firstname="test"))
       app.contact.delete_first_contact()


