from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def add_group(self, group):
        wd = self.wd
        wd.find_element_by_xpath("//a[@href='group.php']").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_footer").send_keys(group.footer_name)
        wd.find_element_by_name("submit").click()

    def add_contact(self, contact):
        wd = self.wd
        wd.find_element_by_xpath("//a[@href='edit.php']").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("submit").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
