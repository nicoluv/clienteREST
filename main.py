from json import JSONDecodeError

import requests
import json

host = "http://localhost:7000"

def crearURL(token=None):
    res = input("\nIndique si desea acceder al api REST [s/n]: ")
    temp = token

    while res != "s" and res != "n":
        res = input("Indique si desea acceder al api REST [s/n]: ")

    if res == "s":
        if token == None:
            token = input("\nIntroduzca su token: ")

        username = input("\nIntroduzca el nombre del usuario para registrar el url: ")
        url = input("\nIntroduzca el url: ");
        my_headers = {'Authorization': 'Bearer ' + token}

        response = requests.post(host + '/api/usuarios/' + username, params={'url': url},
                                 headers=my_headers)

        try:
            print(response.json())
        except JSONDecodeError:
            print("\nToken no existente. Intentelo de nuevo")
            if temp is None:
                token = None
            return crearURL(token)

    elif res == "n":
        exit()

def listarUrlUsuario(token=None):
    res = input("\nIndique si desea acceder al api REST [s/n]: ")

    while res != "s" and res != "n":
        res = input("\nIndique si desea acceder al api REST [s/n]: ")

    if res == "s":
        if token == None:
            token = input("\nIntroduzca su token: ")

        usuario = input("\nIntroduzca el nombre del usuario a buscar: ")
        fecha = input("\nIntroduzca la fecha a consultar [yyyy-MM-dd]: ")
        my_headers = {'Authorization': 'Bearer ' + token}

        response = requests.get(host + '/api/usuarios/' + usuario + "/fecha/" + fecha, headers=my_headers)

        try:
            print(response.json())
        except JSONDecodeError:
            print("\nToken no existente. Intentelo de Nuevo")
            token = None
            return listarUrlUsuario(token)

    elif res == "n":
        exit()

def loginRegistrar():

    res = input("\nIndique si desea obtener un token [s/n]: ")

    while res != "s" and res != "n":
        res = input("\nIndique si desea obtener un token [s/n]: ")

    if res == "s":

        print("\nInicio de sesión - REST\n")

        usuario = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        user = {'usuario': usuario, 'password': password}
        to_json = json.dumps(user)

        response = requests.post(host + "/api/login", data=to_json)

        print("")

        try:
            print(response.json())
            token = json.loads(json.dumps(response.json()))['token']
        except JSONDecodeError:
            print("\nUsuario o Contrasena incorrecta.  Intentelo de Nuevo")
            return loginRegistrar()

        if json.dumps(response.json()).startswith('"Error') == False:
            crearURL(token)

    elif res == "n":
        crearURL()

def loginListar():
    res = input("\nIndique si desea obtener un token [s/n]: ")

    while res != "s" and res != "n":
        res = input("\nIndique si desea obtener un token [s/n]: ")

    if res == "s":

        print("\nInicio de sesión - REST\n")

        usuario = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        user = {'usuario': usuario, 'password': password}
        to_json = json.dumps(user)

        response = requests.post(host + "/api/login", data=to_json)

        print("")

        try:
            print(response.json())
            token = json.loads(json.dumps(response.json()))['token']
        except JSONDecodeError:
            print("\nUsuario o Contrasena incorrecta. Intentelo de Nuevo")
            return loginListar()

        if json.dumps(response.json()).startswith('"Error') == False:
            listarUrlUsuario(token)

    elif res == "n":
        listarUrlUsuario()

print("Bienvenido al clientes REST\n")
resp = input("\n¿Desea registrar o listar ? [1] -Registar Url [2]- Listar Urls de un usuario: ")
while resp != "1" and resp != "2":
    resp = input("\n¿Desea registrar o listar ? [1] -Registar Url [2]- Listar Urls de un usuario: ")
if resp == "1":
    loginRegistrar()
elif resp == "2":
    loginListar()
