from selenium import webdriver

def test_setup():
    global driver
    driver= webdriver.Chrome()
    driver.get("http://localhost:8080/login?from=%2F")
    driver.maximize_window()
    driver.implicitly_wait(30)
def test_login():
    driver.find_element_by_name("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()

def test_logout():
    driver.find_element_by_xpath("//*[text()='log out']").click()

# test_setup()
# test_login()
# test_logout()





