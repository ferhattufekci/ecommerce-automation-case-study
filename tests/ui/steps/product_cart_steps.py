from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

@given('I am on the e-commerce site')
def step_given_i_am_on_the_ecommerce_site(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com")

@when('I log in with valid credentials')
def step_when_i_log_in_with_valid_credentials(context):
    context.driver.find_element(By.ID, "login").click()
    context.driver.find_element(By.ID, "username").send_keys("user")
    context.driver.find_element(By.ID, "password").send_keys("pass")
    context.driver.find_element(By.ID, "submit").click()

@when('I search for "{search_term}"')
def step_when_i_search_for(context, search_term):
    search_box = context.driver.find_element(By.NAME, "search")
    search_box.send_keys(search_term)
    search_box.submit()

@when('I filter the results by price range {price_range}')
def step_when_i_filter_results_by_price_range(context, price_range):
    context.driver.find_element(By.ID, "filter").send_keys(price_range)

@when('I select a random product')
def step_when_i_select_random_product(context):
    products = context.driver.find_elements(By.CLASS_NAME, "product")
    context.product = random.choice(products)
    context.product.click()

@when('I add the product to the cart')
def step_when_i_add_product_to_cart(context):
    seller_ratings = context.driver.find_elements(By.CLASS_NAME, "seller-rating")
    min_rating_seller = min(seller_ratings, key=lambda s: s.text)
    min_rating_seller.find_element(By.NAME, "add-to-cart").click()

@then('I should see the product in the cart')
def step_then_i_should_see_product_in_cart(context):
    context.driver.find_element(By.ID, "cart").click()
    assert "cep telefonu" in context.driver.page_source
    context.driver.quit()