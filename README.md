# AntistalkerBot

Antidote to my 2015 DC Skytalk "Automate Your Stalking".

##### CHANGELOG

###### 06/25/2018 
Currently, all testing is done in a separate working directory. Code will be merged when testing complete.

###### 06/28/2018
Moved a lot of snippets around this session. Worked on a menu system so input is taken in as an argument, either by username or user ID. I can make the menu more functional, but for now it works with minimal iptions.

Taking in username argument seems to work, but there is no output with user ID as an argument. Tried str and int formatting for ID, but no dice. Will troubleshoot this soon. The rest of my sandbox is in the giant multiline comment towards the end of the script. That will disappear as I move snippets around.

###### 06/30/2018
Resolved menu selection issue.
Moved code into proper place depending on flag selectiom.
Resolved Twitter ID option issue, ~~but it broke again when moving code.~~

###### 07/09/2018
Program was being rate limited, So I changed time to sleep from 20 to 60. Increases time of scrape, but no longer gets blocked. Rate Limit chart from Twitter found ehre:
https://developer.twitter.com/en/docs/basics/rate-limits.html .
Rate Limit depends on the nature/type of request.
Also handled file operations whether the file originally exists or not..


_TO-DO_
1. ~~Build menu into program.~~
2. Report default settings of suspect accounts.
3. Resolve Twitter IDs to usernames for human readability.
4. ~~Fix User ID query.... was fixed and broke again. Will review.~~
