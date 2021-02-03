Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameter
    Given I launch firefox browser
    When I open orange HRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to the system with Multiples parameters
    Given I launch firefox browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |