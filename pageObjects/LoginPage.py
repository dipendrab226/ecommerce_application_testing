class LoginPage:
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    # button_login_xpath = "//input[@value='Log in']"
    button_login_class = "buttons"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        login_button = self.driver.find_elements_by_class_name(self.button_login_class)
        login_button[0].click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()