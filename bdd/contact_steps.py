from pytest_bdd import given, when, then
from model.contact import Info
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <name>, <last_name> and <number>')
def new_contact(name, last_name, number):
    return Info(firstname=name, lastname=last_name, homedid=number)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Info(firstname="Test1"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@when('I modify the contact from the list with <name> and <last_name>')
def modify_contact(app, random_contact, name, last_name):
    changed_contact = Info(firstname=name, lastname=last_name)
    app.contact.modify_contact_by_id(random_contact.id, changed_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Info.id_or_max) == sorted(new_contacts, key=Info.id_or_max)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(), key=Info.id_or_max)



@then('the new contact list is equal to the old list with modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, name, last_name, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    changed_contact = Info(firstname=name, lastname=last_name)
    old_contacts.remove(random_contact)
    old_contacts.append(changed_contact)
    assert sorted(old_contacts, key=Info.id_or_max) == sorted(new_contacts, key=Info.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(), key=Info.id_or_max)

