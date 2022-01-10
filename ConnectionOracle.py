import cx_Oracle


class ConnectionDB:
    connection = None


def SetConnection():
    ConnectionDB.connection = cx_Oracle.connect("bd114", "Georgiana16", "bd-dc.cs.tuiasi.ro:1539/orcl")


#def Test_Afisare():
    #cursor = ConnectionDB.connection.cursor()
    # sql_afisare = "select * from PACIENT"
    # cursor.execute(sql_afisare)
    # for result in cursor:
    #     print(result)


def CloseConnection():
    if ConnectionDB.connection:
        ConnectionDB.connection.close()
