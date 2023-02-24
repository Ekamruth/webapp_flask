from flask import Flask, render_template #importing Flask and render template

app=Flask(__name__,template_folder='htmlfiles') #creating a instance of flask or initiating flask and assigning the template folder
@app.route("/") #specify the route

def naruto():
    return render_template('naruto_webpage.html') #specify the html file of the webpage

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

