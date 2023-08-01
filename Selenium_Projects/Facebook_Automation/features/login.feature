Feature: Facebook Login
  As a user I want to log in to Facebook
  So that I can access my account

 Scenario: Successful Login
    Given I am on the Facebook login page
    When I enter my username "mail_id@gmailcom"
    And I enter my password "password"
    And I click the login button
    Then I should be logged in to my account