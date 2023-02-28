
from sqlalchemy import create_engine, text

dbcon_string="mysql+pymysql://peb9zy44l6y7y03zobpd:pscale_pw_6aI0gwsjCau5piw5eHIyZRBiJwh5suBOoE3ckZu4qmE@ap-south.connect.psdb.cloud/naruto?charset=utf8mb4"

engine = create_engine(dbcon_string,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def chars_info():
  with engine.connect() as conn:
    result=conn.execute(text("select * from naruto.characters"))
    result_all=result.all()
  char_dict=[]
  for row in result_all:
    char_dict.append(row._mapping)
  return char_dict

def char_info(name):
  with engine.connect() as conn:
    s=("select * from naruto.characters where name='%s'" %name)
    result=conn.execute(text(s))    
    result_all=result.all()
    single_char_info=[]
    for row in result_all:
      single_char_info.append(row._mapping)
    return single_char_info[0]
    
  
      

  


  
  
  