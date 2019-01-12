import csv
import os


class TableData:
    def __init__(self):
        self.Table = []
        self.TableRows = 0
        self.filename = r'C:\Program Files\Sublime Text 3\moduledata.csv'
        if (not os.path.isfile(self.filename)):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['line', 'total', 'infolders', 'folders'])

    def printTable(self):
        print(self.Table)

    def DataFromCSV(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.Table += [[row['line'], row['total'], row['infolders'], row['folders']]]
                self.TableRows += 1

    def AddToTableFromPath(self, path, recursive=True, hidden=False, venv=False):
        files = []
        if (recursive):
            for (dirpath, dirnames, filenames) in os.walk(path):
                for file in filenames:
                    if ((file[-3:] == '.py') and (dirpath.find('\\.') == -1 or hidden) and (
                            (dirpath.find('\\venv\\') == -1 and dirpath[-5:] != '\\venv') or venv)):
                        files += [dirpath + '\\' + file]
        else:
            for (dirpath, dirnames, filenames) in os.walk(path):
                for file in filenames:
                    if ((file[-3:] == '.py') and (dirpath.find('\\.') == -1 or hidden) and (
                            (dirpath.find('\\venv\\') == -1 and dirpath[-5:] != '\\venv') or venv)):
                        files += [dirpath + '\\' + file]
                break


    def CSVFromData(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['line', 'total', 'infolders', 'folders'])
            for i in range(self.TableRows):
                writer.writerow(self.Table[i])


filename = r'C:\Program Files\Sublime Text 3\moduledata.csv'

t = TableData()
t.DataFromCSV()
t.printTable()
t.AddToTableFromPath(r'B:\питонячие проекты')
# t.CSVFromData(filename)
