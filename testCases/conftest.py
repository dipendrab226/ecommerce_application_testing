import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    BROWSERSTACK_URL = 'https://dipendrabharati1:NNDPfsfz7FrZX5LJkPae@hub-cloud.browserstack.com/wd/hub'
    desired_cap = {
        'os': 'Windows',
        'os_version': '10',
        'browser': browser,
        'browser_version': '89',
        'name': "dipendrabharati1's First Test"
    }
    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

    # if browser == 'chrome':
    #
    #     driver = webdriver.Chrome(executable_path='C:\\Users\\Dibs\\Desktop\\chromedriver_win32\\chromedriver.exe')
    #     print("Launching chrome browser.........")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox(executable_path='C:\\Users\\Dibs\\Desktop\\geckodriver-v0.29.0-win64\\geckodriver.exe')
    #     print("Launching firefox browser.........")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'UI_Automation'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Dipendra'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
