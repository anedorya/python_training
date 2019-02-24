from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, info):
        self.app.return_to_home()
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in personal info
        self.fill_info(info)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home()
        # wd.find_element_by_name("selected[]")


    def modify(self, info):
        self.app.return_to_home()
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill in personal info
        self.fill_info(info)
        # confirm changes
        wd.find_element_by_name("update").click()
        self.app.return_to_home()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_info(self, info):
        wd = self.app.wd
        # fill in personal info
        self.change_field_value("firstname", info.firstname)
        self.change_field_value("middlename", info.middlename)
        self.change_field_value("lastname", info.lastname)
        self.change_field_value("nickname", info.nick)
        self.change_field_value("title", info.title)
        self.change_field_value("company", info.cname)
        self.change_field_value("address", info.address)
        # fill in  phone numbers
        self.change_field_value("home", info.homedid)
        self.change_field_value("mobile", info.cellular)
        self.change_field_value("work", info.workdid)
        self.change_field_value("fax", info.fax)

        # fill in  emails and website
        self.change_field_value("email", info.email)
        self.change_field_value("email2", info.email2)
        self.change_field_value("email3", info.email3)
        self.change_field_value("homepage", info.website)
        # choose birthday and anniversary day
        # wd.find_element_by_name("bday").click()
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        # wd.find_element_by_xpath("//option[@value='15']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        # wd.find_element_by_xpath("//option[@value='November']").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(info.byear)
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text("13")
        # wd.find_element_by_xpath("(//option[@value='13'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        # wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(info.ayear)
        # fill in secondary info

        self.change_field_value("address2", info.address2)
        self.change_field_value("phone2", info.home)
        self.change_field_value("notes", info.notes)


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit contact deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def count(self):
        wd = self.app.wd
        self.app.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))