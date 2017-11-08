*** Settings ***
Library           Process
Library    handling_process.Server    WITH NAME    server_start
Library    Collections
Suite Setup    Start Server
Suite Teardown    Kill server

*** Variables ***
${terminal}    cmd

${command1}    /K appium -p 4723
${command2}    /K appium -p 4750
*** Test Cases ***
Example
*** Keywords ***
Start Server
    ${source_result} =    server_start.open_appium    ${terminal}    ${command1}    ${command2}

    sleep    60
kill server
    ${result} =    server_start.kill_appium
