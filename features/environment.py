

from selenium import webdriver

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()
