Feature: The dealer for the game of 21

Scenario: Deal initial cards
  Given a dealer
  When the round starts
  Then the dealer gives itself two cards

Scenario Outline: Get hand total
  Given a <hand>
  When the dealer sums the cards
  Then the <total> is correct

  Examples: Hands
  | hand          | total |
  | 5,7           | 12    |
  | 5,Q           | 15    |
  | Q,Q,A         | 21    |
  | J,Q,K         | 30    |
  | K,Q,A         | 21    |
  | Q,A           | 21    |
  | A,A,A         | 13    |

Scenario: A Dealer can always play
  Given a dealer
  When the round starts
  Then the dealer chooses a play
