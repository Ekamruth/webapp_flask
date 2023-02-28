from flask import Flask, render_template #importing Flask and render template
from dbconnect import chars_info, char_info

app=Flask(__name__,template_folder='htmlfiles') #creating a instance of flask or initiating flask and assigning the template folder


@app.route("/") #specify the route
def naruto():
    characters=chars_info()
    return render_template('naruto_webpage.html',characters=characters) #specify the html file of the webpage

@app.route("/char_desc/<name>")
def description_character(name):
  char_desc=char_info(name)
  return render_template('char_description.html',char_desc=char_desc)
  


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

