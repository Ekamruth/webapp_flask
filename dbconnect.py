import os
from sqlalchemy import create_engine, text      

#dbcon_string contains the connection string to the database, including the necessary authentication credentials to connect to the database. 
dbcon_string=os.environ['db_con_str']

#creating a database engine
engine = create_engine(dbcon_string,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

#Fetching information about all characters from the characters table in the naruto database.
def chars_info():
  with engine.connect() as conn:
    result=conn.execute(text("select * from naruto.characters"))
    result_all=result.all()
  char_dict=[]
  for row in result_all:
    char_dict.append(row._mapping)
  return char_dict

#Fetching information about a specific character from the characters table in the naruto database.
def char_info(name):
  with engine.connect() as conn:
    s=("select * from naruto.characters where name='%s'" %name)
    result=conn.execute(text(s))    
    result_all=result.all()
    single_char_info=[]
    for row in result_all:
      single_char_info.append(row._mapping)
    return single_char_info[0]
    
  
      

  


  
  
  
