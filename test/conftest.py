from selenium import webdriver
import pytest


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome("/Users/nineleaps/PycharmProjects/pytest-boilerplate/Tests/driver/chromedriver")
    b.implicitly_wait(10)

    yield b
    b.quit()
