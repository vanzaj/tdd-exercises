Feature: Bank account
  Scenario: Cash withdrawal
    Given I have 100 dollars in my account
    When I withdraw 20 dollars
    Then I should have 80 dollars in my account

