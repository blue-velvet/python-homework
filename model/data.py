from sys import maxsize


class Group:
    def __init__(self, group_name=None, group_footer=None, id=None):
        self.group_name = group_name
        self.group_footer = group_footer
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.group_name, self.group_footer)

    def __eq__(self, other):
        return (self.id == None or other.id == None or self.id == other.id) and self.group_name == other.group_name

class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, all_phones_from_home_page=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id == None or other.id == None or self.id == other.id) and self.firstname == other.firstname

    def login(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@type='submit']").click()