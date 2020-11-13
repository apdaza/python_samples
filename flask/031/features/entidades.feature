Feature: Listado entidades

Scenario Outline: Get entities
  Given a data base of banco de preguntas
  When the db was connected
  Then the <entity> was listed

  Examples: entity
  | entity |
  | categoria |
  | tipo_categoria |
  | pregunta |
  | usuario |
  | evaluacion |

Scenario Outline: Get entities fields
  Given a <entity> to show fields
  When the entity was selected
  Then the <fields> are listed

  Examples: entity_fields
  | entity              | fields |
  | tipo_categoria      | tca_id    |
  | categoria           | cat_id    |
  | categoria           | cat_nombre    |
  | pregunta           | pre_texto |
  