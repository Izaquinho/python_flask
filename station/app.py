from urllib import response
from colorama import Cursor
import mysql.connector
from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL,MySQLdb
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

#Banco de dados
mydb = mysql.connector.connect(
 host="localhost",
 port="3306",
 user="root",
 password="root",
 database="itrackerr"
)

#Atualizar localização
@app.route("/update", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def update():
  try:
    data = request.get_json()
    sql=f"UPDATE motoristas SET latitude='{data['latitude']}', longitude='{data['longitude']}' WHERE idMotorista={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Localização atualizada com sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())

#Método Get 
@app.route("/get", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def get():
  try: 
    sql="SELECT * FROM motoristas"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())

#Método Post login
@app.route('/login', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def login():

  try:
    data = request.get_json(force=True) 
    sql=f"SELECT * FROM motoristas WHERE email='{data['email']}' AND senha='{data['senha']}'"
    # print (data['senha'])
    mydb.reconnect()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios_data= []
    response_login = mycursor.fetchall()
    for row in response_login:
        usuarios_list = {
        "idMotorista" : row[0],
        "nomeCompleto" : row[1],
        "senha" : row[2],
        "email" : row[3],
        "cpf" : row[4],
        "rg" : row[5],
        "telefone" : row[6],
        "latitude" : row[7],
        "longitude" : row[8],
        "cnh" : row[9],
      }
    usuarios_data.append(usuarios_list)   
    if (response_login):
      return{"mensagem" : "Sucesso", "data" : usuarios_data}
    else:
      return {"mensagem" : "Error"}
  except Exception as ex:
    return ("error")

def error_error():       
    return jsonify({"mensagem": "Não foi possível concluir a ação!"})


if __name__ == '__main__':
    app.run(DEBUG=True)