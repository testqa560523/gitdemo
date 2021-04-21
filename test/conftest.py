import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver   #python understand that the value of driver should be same globally set here.
    browsername = request.config.getoption("--browser_name")
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:/Users/Admin/Downloads/geckodriver-v0.29.1-win64/geckodriver.exe")
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver  #to set driver class varibale as driver
    yield   #after all the test completed yield will execute at the last.
    driver.close()
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)




