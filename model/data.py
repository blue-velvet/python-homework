class Group:
    def __init__(self, group_name=None, group_footer=None):
        self.group_name = group_name
        self.group_footer = group_footer

class Contact:
    def __init__(self, firstname=None, lastname=None, address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def login(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@type='submit']").click()