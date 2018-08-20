@tag-1
Scenario Outline: User login to linkedin Page
Given I go to LinkedIn page
When I input username as "<username>" in username field
And I input password as "<password>" in password field
And I click on login button
Then UserName of mine is displayed as '<name>'

Examples:
|username              |password  |name    |
|bctuan271095@gmail.com|Weareoneo0|Tuan Bui|