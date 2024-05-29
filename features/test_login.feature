Feature: Login functionality

Scenario Outline: Verify the user can login with valid credentials
    Given I am on carriers edge home page
    When I click login button
    And I enter username <username>
    And I enter password <password>
    And I click go button
    Then I am on the Dashboard

    Examples:
        |username             |password         |
        |validuser@gmail.com  |password         |

    Scenario Outline: Verify the user can not login with invalid credentials
        Given I am on carriers edge home page
        When I click login button
        And I enter username <username>
        And I enter password <password>
        And I click go button
        Then I verify there is an error
    
        Examples:
            |username               |password         |
            |invaliduser@gmail.com  |wrong_password   |
            |invaliduser@gmail.com  |                 |
            |                       |wrong_password   |
            |                       |                 |
    