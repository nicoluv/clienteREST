import requests
import json


def crearURL(token=None):
    res = input("\nIndique si desea acceder al api REST [s/n]: ")

    while res != "s" and res != "n":
        res = input("Indique si desea acceder al api REST [s/n]: ")

    if res == "s":
        if token == None:
            token = input("\nIntroduzca su token: ")

        username = input("\nIntroduzca el nombre del usuario para registrar el url: ")
        url = input("\nIntroduzca el url: ");
        my_headers = {'Authorization': 'Bearer ' + token}

        response = requests.post('http://localhost:7000/api/usuarios/' + username, params={'url': url},
                                 headers=my_headers)

        print(response.json())

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
        my_headers = {'Authorization': 'Bearer ' + token}

        response = requests.get('http://localhost:7000/api/usuarios/' + usuario, headers=my_headers)

        print(response.json())

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

        response = requests.post("http://localhost:7000/api/login", data=to_json)

        print("")
        print(response.json())

        token = json.loads(json.dumps(response.json()))['token']

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

        response = requests.post("http://localhost:7000/api/login", data=to_json)

        print("")
        print(response.json())

        token = json.loads(json.dumps(response.json()))['token']

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
