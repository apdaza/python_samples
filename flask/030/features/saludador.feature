Feature: Saludador

Scenario Outline: Get hello user
  Given a <name> to greet
  When the greeter greets the names
  Then the <greet> of name is correct

  Examples: names
  | name       | greet |
  | juan        | Hello juan as Guest    |
  | maria       | Hello maria as Guest    |
  | ana         | Hello ana as Guest    |
  | admin       | Hello Admin  |
