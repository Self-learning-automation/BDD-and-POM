@signup
  Feature: User sign up
    As a user I want to sign up to the system

  @case-1
  Scenario Outline: Signup - Verify user sign up successfully
    Given User is in the php_travel page
    When the user click on My Account in the homepage
    And the user click on Sign Up in My Account
    And the user input first name as "<first_name>" in the sign up page
    And the user input last name as "<last_name>" in the sign up page
    And the user input phone as "<phone>" in the sign up page
    And the user input email in the sign up page
    And the user input password as "<password>" in the sign up page
    And the user input confirm password as "<confirm_password>" in the sign up page
    And the user click on Sign up button in the sign up page
    Then Verify redirect user to profile page, first name as "<first_name>" and last name as <"last_name"> displays correctly

    Examples:
      |  |
