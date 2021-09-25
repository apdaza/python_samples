Feature: Calculadora

Scenario Outline: obtener la suma total
    Given a <values> to sum 
    When the calc sum the values
    Then the <total> is ok

    Examples: values
    | values   | total  |
    | 3,2      | 5     |
    | 5,7      | 12     |
    | -1,3     | 2      |
    | 22,100    | 122 |

Scenario Outline: obtener el producto total
    Given a <values> to times 
    When the calc time the values
    Then the <product> is ok

    Examples: values
    | values   | product  |
    | 3,2      | 6     |
    | 5,7      | 35     |
    | -1,3     | -3      |
    | 22,100    | 2200 |

Scenario Outline: obtener el resultado de la resta
    Given a <values> to substract
    When the calc substract the values
    Then the <total> is ok

    Examples:
        | values | total |
        | 1,3  | -2  |
        | -3,-2 | -1 |
        | 5,2 | 3 |