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
 password="",
 database="itrackerr"
)

#Atualizar localização
@app.route("/updateandroid", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def update():
  try:
    data = request.get_json()
    sql=f"UPDATE motoristas SET latitude='{data['latitude']}', longitude='{data['longitude']}' WHERE idMotorista={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    mydb.commit()
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
        x = row[0]      
    if (response_login):
      return str(x)
    else:
      return str("erro")
  except Exception as ex:
    return (ex)

#Get coletas
@app.route("/getColetas", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getColetas():
  try: 
    data = request.get_json(force=True) 
    sql=f"SELECT * FROM registrocoleta WHERE Motoristas_idMotorista = '{data['id']}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    dataMotoristas = mycursor.fetchall()
    usuarios_data = []
    for row in dataMotoristas:
      usuarios_list = {
        "idRegistroColeta" : row[0],
        "dataColeta" : row[1],
        "horaColeta" : row[2],
        "estadoColeta" : row[3],
        "cidadeColeta" : row[4],
        "bairroColeta" : row[5],
        "ruaColeta" : row[6],
        "numeroColeta" : row[7],
        "dataEntrega" : row[8],
        "horaEntrega" : row[9],
        "estadoEntrega" : row[10],
        "cidadeEntrega" : row[11],
        "bairroEntrega" : row[12],
        "ruaEntrega" : row[13],
        "numeroEntrega" : row[14],
        "nomeCliente" : row[15],
        "cnpjCliente" : row[16],
        "emailCliente" : row[17],
        "telefoneCliente" : row[18],
        "pesoCarga" : row[19],
        "volumeCarga" : row[20],
        "valorCarga" : row[21],
        "Ocorrencia_idOcorrencia" : row[22],
        "Motoristas_idMotorista" : row[23],
    }
      usuarios_data.append(usuarios_list)
    return str(usuarios_data)
  except Exception as ex:
    return str("Não existem coletas para você")

def error_error():       
    return jsonify({"mensagem": "Não foi possível concluir a ação!"})

if __name__ == '__main__':
    app.run(DEBUG=True)