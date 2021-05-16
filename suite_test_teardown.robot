*** Settings ***
library  test.py
suite setup  test_appium  4723
suite teardown  log to console  close appium server
test setup  log to console  test entry
test teardown  log to console  second last entry
*** Variables ***
*** Test Cases ***
Make call from one phone to another
    Call A to B
    Answer from phone B
    End the call from B

Make comfrence call from one phone to another

Make sms from one phone to another
Make wtsapp call from one phone to another
Make wifi call from one phone to another
*** Keywords ***
Call A to B
Answer from phone B
End the call from B
test setup
    log to console  overwritetest setup