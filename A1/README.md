Notes from Team Constant State of Tears: 

1. After much debate, our team decided to have local constants in the Profile module. We decided to do this because 
our menu needs to display menu options before we instantiate necessary subclasses and the best way we found to
provide this information is to use these constants to populate our menu options for the user. 

2. After looking through the assignment's directions discussing different ways to approach implementing warnings/
notifications/lockout messages, we took the approach that if, for example, a user exceeds a budget threshold milestone,
even if other milestones are reached (like if a warning is triggered at 50% of a budget and a notification at 100%), all
milestone alerts will keep triggering, e.g., if a warning was triggered at a lower threshold, that warning will still
trigger when a higher threshold alert is reached and its corresponding alert triggered. 