import os, json, shutil

__dir__ = "database/data/"

def createTable(tableName):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    try:
        tableName = str(tableName)
    except:
        return "invalid 'tableName'"

    if os.path.isdir(__dir__+tableName):
        return "table is ready"
    else:
        try:
            os.mkdir(__dir__+tableName)
            return "table created"
        except:
            return "error"

def deleteTable(tableName):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    try:
        tableName = str(tableName)
    except:
        return "invalid 'tableName'"

    if not os.path.isdir(__dir__+tableName):
        return "table not found"
    else:
        try:
            shutil.rmtree(__dir__+tableName)
            return "table deleted"
        except:
            return "error"

def addColumn(tableName, data):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    elif tableName == "" or tableName == None:
        return "invalid 'data'"

    try:
        tableName = str(tableName)
    except:
        return "invalid 'tableName'"

    if not os.path.isdir(__dir__+tableName):
        return "table not found"
    else:
        is_column = 1
        while True:
            if os.path.isfile(__dir__+tableName+"/"+str(is_column)+"_column.json"):
                is_column+=1
            else:
                try:
                    open_column = open(__dir__+tableName+"/"+str(is_column)+"_column.json", "w")
                    if data != False or data != "":
                        open_column.write(json.dumps(data, indent=4))
                    else:
                        open_column.write("{}")
                    open_column.close()
                    return "column created"
                    break
                except:
                    return "error"
                    break

def updateColumn(tableName, columnId, data):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    elif columnId == "" or columnId == None:
        return "invalid 'columnId'"
    elif tableName == "" or tableName == None:
        return "invalid 'data'"

    try:
        tableName = str(tableName)
        columnId = int(columnId)
    except:
        return "invalid arguments"


    try:
        open_column = open(__dir__+tableName+"/"+str(columnId)+"_column.json","w")
        open_column.write(json.dumps(data, indent=4))
        open_column.close()
        return "column updated"
    except:
        return "error"

def printColumn(tableName, columnId):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    elif columnId == "" or columnId == None:
        return "invalid 'columnId'"

    try:
        tableName = str(tableName)
        columnId = int(columnId)
    except:
        return "invalid arguments"

    try:
        open_column = open(__dir__+tableName+"/"+str(columnId)+"_column.json", "r")
        column = json.loads(open_column.read())
        open_column.close()
        return column
    except:
        return "error"

def listColums(tableName, startId, limit):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    elif startId == "" or startId == None:
        return "invalid 'startId'"
    elif limit == "" or limit == None:
        return "invalid 'limit'"

    try:
        tableName = str(tableName)
        startId = int(startId)
        limit = int(limit)
    except:
        return "invalid arguments"
    if startId <= 0:
        startId = 0
    if limit <= 0:
        limit = 0
    if limit > 15:
        limit = 15

    list = []
    column_id = startId
    while column_id <= startId+limit-1:
        if os.path.isfile(__dir__+tableName+"/"+str(column_id)+"_column.json"):
            open_column = open(__dir__+tableName+"/"+str(column_id)+"_column.json", "r")
            column = json.loads(open_column.read())
            list.append(column)
        column_id+=1

    return list

def listColumsSecret(tableName, startId, limit):
    if tableName == "" or tableName == None:
        return "invalid 'tableName'"
    elif startId == "" or startId == None:
        return "invalid 'startId'"
    elif limit == "" or limit == None:
        return "invalid 'limit'"

    try:
        tableName = str(tableName)
        startId = int(startId)
        limit = int(limit)
    except:
        return "invalid arguments"
    if startId <= 0:
        startId = 0
    if limit <= 0:
        limit = 0
    if limit > 15:
        limit = 15

    list = []
    column_id = startId
    while column_id <= startId+limit-1:
        if os.path.isfile(__dir__+tableName+"/"+str(column_id)+"_column.json"):
            open_column = open(__dir__+tableName+"/"+str(column_id)+"_column.json", "r")
            column = json.loads(open_column.read())
            list.append(column[1])
        column_id+=1

    return list

