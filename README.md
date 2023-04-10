# webapp_flask

1. This Flask application renders a web page that displays information aboout characters in the Naruto anime/manga. The characters' information is stored in a MySQL database that is connected to the Flask app using the 'dbconnect.py' file.
2. The landing page has the route '/' whose template is rendered using the 'naruto_webpage.html' file that displays the list of characters using the dbconnect file. 
3. The dbconnect file connects to a MySQL database, retrieves information about characters in the Naruto universe and returns the data in the form of a dictionary. It uses the SQLAlchemy library to create a connection with the database and retrieve information.
4. The code consists of two functions:
  1.	chars_info(): It retrieves all character information from the "naruto.characters" table and returns it in the form of a dictionary.
  2.	char_info(name): It retrieves a single character's information from the "naruto.characters" table, based on the name provided in the function argument and returns it in the form of a dictionary.
5. The code uses the dbcon_string variable to connect to the MySQL database. It uses the create_engine() function of the SQLAlchemy library to create a connection object, passing the database connection string and the SSL certificate path as arguments to the function.
6. The chars_info() function uses the connect() method of the engine object to connect to the database and the execute() method to run the SQL query "select * from naruto.characters". It then uses the all() method to retrieve all rows of data and appends them to a list of dictionaries called char_dict. The function then returns the char_dict list. 
7. The redirected pages have the route '/char_desc/<name>' which displays the information about the specified character.

