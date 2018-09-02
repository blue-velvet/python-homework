class SessionHelper:
    def __init__(self, app, username=None, password=None):
        self.app = app
        self.username = username
        self.password = password

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as():
                return
            else:
                self.logout()
        self.login(username, password)


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in() > 0:
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))

    def is_logged_in_as(self, username='admin'):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text == "(" + username + ")"
