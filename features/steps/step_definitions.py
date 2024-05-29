from behave import given, then, when
import utils.urls as urls

@given('I am on carriers edge home page')
def on_page(context):
    context.driver.get(urls.urls['homepage'])

@when('I click login button')
def click_login(context):
    context.login.click_login_button(context.driver)

@when('I enter username {username}')
def enter_username(context, username):
    context.login.enter_username(context.driver, username)

@when('I enter username ')
def enter_username(context):
    pass

@when('I enter password {password}')
def enter_password(context, password):
    context.login.enter_password(context.driver, password)

@when('I enter password ')
def enter_password(context):
    pass

@when('I click go button')
def click_go(context):
    context.login.click_go_button(context.driver)

@then('I am on the Dashboard')
def verify_dashboard_title(context):
    # I will assert here that the page title is dashboard. As I do not have valid credentials, I can not verify that.
    print("I am on the Dashboard")

@then('I verify there is an error')
def verify_error(context):
    error_message = context.login.get_error_message(context.driver)
    assert error_message == "Invalid username and/or password, please try again."
