#   CHANGELOG

## 3/29/2025
- able to pull table rows with date of word used and word itself
- created regex to format id, word, and date from table row
- updated Word model with date used column, can get values for used words (num, date) but need to work on formatting date so it can be inserted into db
## 3/28/2025
- Guesses function almost done, returned words that did NOT contain all characters that user identified are in word
- started on db creation, can add all words to db, started work on getting dates from site of when words were used

## 1/24/2025
guess func working as expected, tried tweaking remove word func to make it easier to quit ran into issues, need to troubleshoot

## 1/15/2025
finally able to get guesses but got too many, going to have ChatGPT troubleshoot

## 1/12/2025
- updated words left and removed copy of it
- started work on guesses function

## 1/11/2025
- added update used words list
- created file and function to remove used words from wevsite

## 7/19/2024
added quit at anytime functionality, removed all words up until this point, remove word function is working as expected (so far). Started work on Guesses function

## 6/3/2024 ##
resolved issue with finding word in list
need to add validator for input

## 6/2/2024 ## 
added gitignore, updated words left file
got starter word and main menu functions working
started work on remove word method, able to find word but need to found word