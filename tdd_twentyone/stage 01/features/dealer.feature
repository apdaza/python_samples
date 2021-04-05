Feature: The dealer for the game of 21

Scenario: Deal initial cards
  Given a dealer
  When the round starts
  Then the dealer gives itself two cards
