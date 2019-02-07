import csv

csv.register_dialect('addQuoteDialect',
quoting = csv.QUOTE_ALL,
skipinitialspace = True)

def getColumnNumber(header, filePath):
    with open(filePath, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if row.index(header) + 1:
                colNumber = row.index(header)
                return colNumber
            else:
                print("Column header not found")
                break

def appendLine(stringList, filePath):
    with open(filePath, "a") as f:
        writer = csv.writer(f, dialect = 'addQuoteDialect')
        writer.writerows(stringList)


def modifyValue(row, col, value, filePath):
    with open(filePath, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        lines = list(reader)
        print(lines[row])

# TESTING
path = '../test.csv'
lists = [['append','this'],['to','file']]

print(getColumnNumber('Id', path))
appendLine(lists, path)
modifyValue(1, 3, '342', path)
