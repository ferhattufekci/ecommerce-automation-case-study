import pytest
from selenium import webdriver

@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.funcargs['driver']
        driver.save_screenshot(f"screenshots/{report.nodeid}.png")