import re
from model.contact import Info
from random import randrange

# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
#
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homedid == contact_from_edit_page.homedid
#     assert contact_from_view_page.cellular == contact_from_edit_page.cellular
#     assert contact_from_view_page.workdid == contact_from_edit_page.workdid
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter (lambda x: x is not None,
                                                            [contact.homedid, contact.cellular, contact.workdid, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter (lambda x: x is not None,
                                                            [contact.email, contact.email2, contact.email3]))))


# def test_params_on_home_page(app):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#


def test_all_params_on_home_page(app, orm):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Info.id_or_max)
    contacts_from_db = orm.get_contact_list()
    assert contacts_from_db == sorted(contacts_from_home_page, key=Info.id_or_max)
    n = 0
    for contact in contacts_from_home_page:
        assert contact.firstname == contacts_from_db[n].firstname.strip()
        assert contact.lastname == contacts_from_db[n].lastname.strip()
        assert contact.address == contacts_from_db[n].address.strip()
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[n])
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[n])
        n = n + 1



