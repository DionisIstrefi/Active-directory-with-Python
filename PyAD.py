import csv
from pyad import *
def createuserfromcsv():
    #File path
    file = input('please type your file path + file: ')
    data = open(file,encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    #Loading the Administrator info and server -  NOTE! Server is not shown for security reasons.
    pyad.set_defaults(ldap_server="ldap://localhost:389",username="Administrator",password="E1n5tein!!P455wrd!")

    for line in data_lines[1:]:
        user = line[0]
        oupath = line[2]
        #Info taken from created CSV File.
        ou = pyad.adcontainer.ADContainer.from_dn(oupath)
        #Users,OU,Password pre created in the CSV File.
        pyad.aduser.ADUser.create(user,ou,password="Generic!!P455wrd!")
