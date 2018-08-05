class GroupHelper:
    def __init__(self, app):
        self.app = app

    def add(self, group):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='group.php']").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_footer").send_keys(group.footer_name)
        wd.find_element_by_name("submit").click()