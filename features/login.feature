
Feature: Zen Portal Login Functionality

  Scenario: Validate username and password input boxes
    Given I navigate to Zen Portal
    Then I validate username and password input boxes

  Scenario: Validate submit button
    Given I navigate to Zen Portal
    Then I validate submit button is working

  Scenario: Successful login to Zen Portal
    Given I navigate to Zen Portal
    When I login with valid username and password
    Then I should be logged in successfully

  Scenario: Unsuccessful login to Zen Portal
    Given I navigate to Zen Portal
    When I login with invalid username and password
    Then I should not be logged in successfully

  Scenario: Validate logout functionality
    Given I navigate to Zen Portal
    When I login with valid username and password
    Then I logout from Zen Portal