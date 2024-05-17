Citation Finder Web Application

This is a Flask web application that fetches data from a paginated API, identifies citations from the response text, and displays them in a user-friendly format.

Features:
      Fetches data from a paginated API endpoint.
      Identifies citations by checking for common words between the response text and sources' context.
      Displays citations with response text in a user-friendly HTML format.

Prerequisites
Python 3.x installed on your system.

Flask library (flask) installed. You can install it via pip:
pip install flask

Usage
1.Run the Flask application:
       python app.py
       
2.Open a web browser and go to http://127.0.0.1:5000/ to access the application.

3.You should see the citations displayed on the web page, fetched from the API and identified based on common words.

Customization
You can customize the HTML template (index.html) in the templates directory to change the appearance of the web page.
Adjust the logic in identify_citations function in app.py to improve citation identification based on your requirements.
  
