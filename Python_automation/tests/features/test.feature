Feature: Create SSO account online low priority
  #  MMTEST-142
@sitNightly
Scenario Outline:
  Given that I am a colleague member without an SSO account
  And I enter my card number, name and birthdate on the MM website
  And I click Link Account
  When I enter a unique username and a password with character <character>
  #Then I am taken to the Membership Home Page
  Then I am taken to the Payment Page containing <Card Number>, <mm>, <yy>, and <CVV>

Examples:
  |Card Number 	   |mm|yy|CVV|DigitPlace|Number|character|
  |5133333333333338|05|21|222|11        |7     |!        |
  |5133333333333338|05|21|222|11        |7     |#        |
  |5133333333333338|05|21|222|11        |7     |$        |
  |5133333333333338|05|21|222|11        |7     |&        |
  |5133333333333338|05|21|222|11        |7     |*        |
  |5133333333333338|05|21|222|11        |7     |/        |
  |5133333333333338|05|21|222|11        |7     |=        |
  |5133333333333338|05|21|222|11        |7     |?        |
  |5133333333333338|05|21|222|11        |7     |^        |
  |5133333333333338|05|21|222|11        |7     |`        |
  |5133333333333338|05|21|222|11        |7     |~        |
