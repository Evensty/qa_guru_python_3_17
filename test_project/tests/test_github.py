from selene.support.conditions import be
from selene.support.shared import browser


def test_github():
    browser.open('https://github.com/')
    browser.element('[name="q"]').should(be.blank)
