class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php']").click()
        self.fill_form(contact)
        wd.find_element_by_name("submit").click()

    def fill_form(self, contact):
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("address", contact.address)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("[src='icons/pencil.png']").click()
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
