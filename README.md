
-------------------------------------------------------------------------
          	             SEPT WEATHER
-------------------------------------------------------------------------

A weather service web application built using the python Flask framework.

-------------------------------------------------------------------------
TEAM MEMBERS AND CONTRIBUTION PERCENT:
-------------------------------------------------------------------------

Ben Diep           s3462344    25%			 
Damon Toumbourou   s3019592    25%
Alex Cheong        s3436036    25%
Doeun Shin         s3392298    25%
  

-------------------------------------------------------------------------
TUTOR:
-------------------------------------------------------------------------
A Homy Ash - Friday 8:30 AM at 14.09.23


--------------------------------------------------------------------------
TECHNICAL STUFF:
--------------------------------------------------------------------------

FRAMEWORK: 
----------
We used Flask a Python web framework with built-in development server 
and debugger. It includes Jinja2 for templating we took advantage of.

FRONT-END:
----------
We used Javascript for the front-end.
Our application features AJAX for serving dynamic content on our pages. 

BACKEND:
--------
We used Python and as mentioned the Flask framework.
Our application uses the MVC design. Python flask handles the routes and 
controllers serves the views and handles database queries.

DATABASE:
---------
We used sqlite3 which is built in to python and flask includes some helpful
functions for dealing with databases.

SCRAPING THE DATA:
------------------
We used the Python modules Beautiful Soup and requests to scrape the html 
from the BOM. 

API:
----
Our site can be used as an API for other programmers. By sending a 
string to our site containing the url of the weather station you wish 
to view our application will return the data in JSON format.

--------------------------------------------------------------------------
REQUIREMENTS: the Python modules required to run our program
--------------------------------------------------------------------------
Note: the requirements are found in the requirements.txt file
-----
Flask==0.10.1
requests=2.9.1
bs4=4.4.1
re=2.2.1
json=2.0.9

--------------------------------------------------------------------------
INSTALATION:
--------------------------------------------------------------------------
Note: the /project-page/HOWTO.txt file contains instructions on installing
----- and running the application

--------------------------------------------------------------------------
TESTING:
--------------------------------------------------------------------------

Unit Testing:
-------------
Our Application includes a Test file: sept-test.py 
This file runs a number of unit tests that call our api urls and functions
and check the return data is as expected.

To run the tests file:
    python sept-test.py
    

System Level Test Cases:
----------------------- 
We have also demonstrated a number of system level test cases the results 
are stored in /project-page/system-tests.pdf
 

--------------------------------------------------------------------------
END OF README
--------------------------------------------------------------------------
