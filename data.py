class Group:
    def __init__(self, group_name, footer_name):
        self.group_name = group_name
        self.footer_name = footer_name

class Contact:
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def login(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@type='submit']").click()