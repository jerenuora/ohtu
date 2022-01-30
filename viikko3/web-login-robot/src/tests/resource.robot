*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Register Page Should Be Open
    Title Should Be  Register

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Page Should Contain Too Short Password
    Page Should Contain  Password is required to be atleast 8 characters long

Register Page Should Contain Invalid Username
    Page Should Contain  Invalid username

Register Page Should Contain Passwords Dont Match
    Page Should Contain  Passwords do not match
Go To Login Page
    Go To  ${LOGIN URL}

Go To Main Page
    Go To  ${HOME URL}

Go To Register Page
    Go To  ${REGISTER URL}