Feature: Product Cart Management

  Scenario: Add a product to the cart
    Given I am on the e-commerce site
    When I log in with valid credentials
    And I search for "cep telefonu"
    And I filter the results by price range 15000 - 20000
    And I select a random product
    And I add the product to the cart
    Then I should see the product in the cart
