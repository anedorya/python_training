Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <name>, <last_name> and <number>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | name  | last_name      | number       |
    | name1 | last_name1     | number1      |
    | name2 | last_name2     | number2      |


Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I modify the contact from the list with <name> and <last_name>
    Then the new contact list is equal to the old list with modified contact

    Examples:
    | name  | last_name      |
    | name9 | last_name9     |