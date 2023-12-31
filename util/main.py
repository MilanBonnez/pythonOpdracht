import db.ManageDb as manageDb
import domain.requestCsv

def printCommandos():
    print("Mogelijke commando's:")
    print("'getTable' Geef alle studenten of alle docenten weer")
    print("'generateCsvFile' Geef een tabel naar keuze weer in de vorm van een csv-file")
    print("'deletePerson' Verwijder een persoon uit een tabel")
    print("'addPerson' Voeg een persoon toe aan een tabel")
    print("'showPerson' Zoek een persoon op uit een bepaalde tabel")
    print("'exit' Ga uit de applicatie")

def generateCsvFile(db):

    tables = ["teachers", "students"]
    print("\nTables:")
    for table in tables:
        print(f"{table}")

    table_name = input("\nKies welke tabel je wil genereren in een csv-file: ")
    
    if table_name not in tables:
        print("\nTabel bestaat niet, kies een tabel die wel bestaat!")
    else:
	    data = manageDb.getTable(table_name)
	    requestCsv.generateCsv(data, filename)
	    print("\nCSV-report maken is gelukt!")

def getTable():
    table = input("Geef de tabel in die je wil weergeven: ")
    manageDb.getTable(table)

def addPerson():
	table = input("In welke tabel moet deze persoon komen te staan? ")
	firstName = input("Voornaam: ")
    lastName = input("Familienaam:")
    manageDb.addPerson(table, firstName, lastName)
    print("\nPersoon is toegevoegd!")

def deletePerson:
	table = input("Uit welke tabel moet deze persoon verwijderd worden?")
	personId = input("Id: ")
    manageDb.addPerson(table, personId)
    print("\nPersoon is vewijders!")

def showPerson:
	table = input("Uit welke tabel komt de persoon die je zoekt?")
	personId = input("Id: ")
	manageDb.showPerson(table, personId)


if __name__ == '__main__':
    printCommandos()
    inputUser = input("Geef een commando mee: ")

    if inputUser == "getTable":
        getTable()
    elif inputUser == "generateCsvFile":
        generateCsvFile(db)
    elif inputUser == "addPerson":
        addPerson()
    elif inputUser == "deletePerson":
        deletePerson()
    elif inputUser == "showPerson":
        showPerson()
    elif inputUser == "exit":
        print("\nApplicatie afsluiten!")
        break


