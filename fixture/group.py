class GroupHelper:
    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='group.php']").click()

    def add(self, group):
        wd = self.app.wd
        self.go_to_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        wd.find_element_by_name("submit").click()
        self.go_to_group_page()

    def fill_form(self, group):
        self.type("group_name", group.group_name)
        self.type("group_footer", group.group_name)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify(self, group):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group()
        wd.find_element_by_name("edit").click()
        self.type("group_name", group.group_name)
        wd.find_element_by_name("update").click()
        self.go_to_group_page()

    def delete(self):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group()
        wd.find_element_by_name("delete").click()
        self.go_to_group_page()
