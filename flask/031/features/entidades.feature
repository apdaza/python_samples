Feature: Listado entidades

Scenario Outline: Get entities fields
  Given a <entity> to show fields
  When the entity was selected
  Then the <fields> are listed

  Examples: entities
  | entity              | fields |
  | tipo_categoria      | tca_id    |
  | categoria           | cat_id    |
  | categoria           | cat_nombre    |
  