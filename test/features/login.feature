Feature: Login_check
  Testing Login from Google Login Screen


  Scenario Outline: 1. Verify if the error message is displayed when user gives wrong Password
    Given User is providing valid URL
    And User is providing valid <Username>
    And Clicks the next button
    And User is providing valid <Password>
    Then click on next button

    Examples:
      | Username | Password |
      |  aravind@yopmail.com   |  aravsjb1312  |