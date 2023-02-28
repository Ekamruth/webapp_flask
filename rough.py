#@app.route("/api/characters")
#def char_description():
 # characters=chars_info()
  #return jsonify(characters)


name=input()
s=("select * from naruto.characters where name='%s'" %name)
print(s)
print(type(s))