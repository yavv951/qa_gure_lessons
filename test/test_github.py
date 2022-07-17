import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from test.locators import LocatorsPageGitHub

URL = 'https://github.com'
REPOSITORY_NAME = 'eroshenkoam/allure-example'
ISSUE_VALUE = '#76'


def test_selene():
    """
     Чистый Selene (без шагов)
    """
    browser.open(URL).driver.set_window_rect(width=1920, height=1080)
    s(LocatorsPageGitHub.SEARCH_ELEMENT).click()
    s(LocatorsPageGitHub.SEARCH_ELEMENT).send_keys(REPOSITORY_NAME)
    s(LocatorsPageGitHub.SEARCH_ELEMENT).submit()
    s(by.link_text(REPOSITORY_NAME)).click()
    s(LocatorsPageGitHub.ISSUE_TAB).click()
    s(by.partial_text(ISSUE_VALUE)).should(be.visible)


def test_lambda_steps():
    """
    Лямбда шаги через with allure.step
    """

    with allure.step(f'Open: {URL}'):
        browser.open(URL).driver.set_window_rect(width=1920, height=1080)

    with allure.step(f'Find repository: {REPOSITORY_NAME}'):
        s(LocatorsPageGitHub.SEARCH_ELEMENT).click()
        s(LocatorsPageGitHub.SEARCH_ELEMENT).send_keys(REPOSITORY_NAME)
        s(LocatorsPageGitHub.SEARCH_ELEMENT).submit()

    with allure.step(f'Choice repository: {REPOSITORY_NAME}'):
        s(by.link_text(REPOSITORY_NAME)).click()

    with allure.step('Open tab Issues'):
        s(LocatorsPageGitHub.ISSUE_TAB).click()

    with allure.step(f'Check Issue with name: {ISSUE_VALUE}'):
        s(by.partial_text(ISSUE_VALUE)).should(be.visible)


def test_decorator_steps():
    """Шаги с декоратором @allure.step"""
    open_browser()
    find_repository()
    choise_repository()
    open_tab_issues()
    check_issue_with_name()


@allure.step(f'Open: {URL}')
def open_browser():
    """
    Open page
    """
    browser.open(URL).driver.set_window_rect(width=1920, height=1080)


@allure.step(f'Find repository: {REPOSITORY_NAME}')
def find_repository():
    """
    Search for repository
    """
    s(LocatorsPageGitHub.SEARCH_ELEMENT).click()
    s(LocatorsPageGitHub.SEARCH_ELEMENT).send_keys(REPOSITORY_NAME)
    s(LocatorsPageGitHub.SEARCH_ELEMENT).submit()


@allure.step(f'Choice repository: {REPOSITORY_NAME}')
def choise_repository():
    """
    Go to repository
    """
    s(by.link_text(REPOSITORY_NAME)).click()


@allure.step('Open tab issues')
def open_tab_issues():
    """
    Open issue tab
    """
    s(LocatorsPageGitHub.ISSUE_TAB).click()


@allure.step(f'Check Issue with name: {ISSUE_VALUE}')
def check_issue_with_name():
    """
    Check issue by name
    """
    s(by.partial_text(ISSUE_VALUE)).should(be.visible)


@allure.tag('WEB UI')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'yadutovvv')
@allure.feature('Testing github with selene')
@allure.story(f'Найти номер задачи {ISSUE_VALUE}')
@allure.link('https://github.com/yavv951', name='Owner')
def test_decorator_steps_with_label():
    """
    Test with labels
    """
    test_decorator_steps()
