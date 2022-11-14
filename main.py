from flask import Flask, Response, request
from config import name, surname
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    demo_variable = 'hoşgeldiniz'
    return demo_variable

@app.route('/name-username', methods=['POST'])
def get_name_surname():

    end_username = name
    end_surname = surname
    name_surname = f'{end_username}  {end_surname}'
    return name_surname



app.run(host='localhost', port=5000)

#Biz sadece postmanden get atalım, ekranda hoşgeldiniz yazsın dönen repsonse

#Sonra post atalım post attığımız body’deki isimi soy ismi alsın toplasın
#öyle response dönsün