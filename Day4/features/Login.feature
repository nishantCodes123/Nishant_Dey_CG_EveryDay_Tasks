Feature: Login Feature

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters invalid credentials
    And clicks the login button
    Then the user should see an error message

  @smoke
  Scenario Outline: Verify login with multiple users
    Given the user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user should see an error message

    Examples:
      | username                | password |
      | standard_user           | secret   |
      | problem_user            | secret   |
      | performance_glitch_user | secret   |
      | error_user              | secret   |
      | visual_user             | secret   |

  Scenario Outline: Verify login with multiple users
    Given the user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user should be redirected to the dashboard

    Examples:
      | username                | password     |
      | standard_user           | secret       |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
      | error_user              | secret_sauce |
      | visual_user             | secret_sauce |
