from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time
import pytest

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    driver.get("https://example.com")
    
    # User login
    driver.find_element(By.ID, "login").click()
    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("pass")
    driver.find_element(By.ID, "submit").click()
    
    # Search for product
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("cep telefonu")
    search_box.submit()
    
    # Filter results
    driver.find_element(By.ID, "filter").send_keys("15000 - 20000")
    
    # Select random product
    products = driver.find_elements(By.CLASS_NAME, "product")
    product = random.choice(products)
    product.click()
    
    # Add to cart
    seller_ratings = driver.find_elements(By.CLASS_NAME, "seller-rating")
    min_rating_seller = min(seller_ratings, key=lambda s: s.text)
    min_rating_seller.find_element(By.NAME, "add-to-cart").click()
    
    # Verify item in cart
    driver.find_element(By.ID, "cart").click()
    assert "cep telefonu" in driver.page_source