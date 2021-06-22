# ecommerce_application_testing
# Highlights from the project
- Automated end to end testing of an ecommerce application website.
- Utilized python, selenium, pytest for creating the test cases. 
- Utilized Page Object Model to separate the locators and actual test cases. 
- Utilized openpyxl to retrieve data from excel sheet for data -driven testing. 
- Generated html reports for the test cases using pytest-html. 
- Generated logs using custom logger created using logging class. 
- Used config files to store to common data and setup method get the driver. 
- Performed the tests locally using Selenium Grid as well as remotely using BrowserStack.


# Challenges during the course of the project
- Some of the challenges that I faced during the project were:
    1. Difficulty in identifying the web elements. Some of them would stop working after a while.
    2. The speed of the webdriver was also an issue because as it was too fast and its speed couldn't be manipulated as the setspeed functions were not application anymore.
    
# Solutions to the challenges during the course of the project
- Some of the solution to the forementioned challenges were:
    1. Trying out different locators to identify the web elements
    2. Using implicit as well as explicit waits to slow down the speed of the driver. Sometimes sleep method was also used.
    3. Using Selenium IDE to track the path of the driver and to identify errors.
