import csv
import os


class CSVReader:
    def __init__(self):
        self.Table = []
        self.TableRows = 0
        self.totalFiles = 0
        self.totalFolders = 0
        self.filename = 'C:\\ProgramData\\Sublime Text 3\\moduledata.csv'
        self.metafilename = 'C:\\ProgramData\\Sublime Text 3\\metadata.txt'
        if (not os.path.isfile(self.filename)):
            if (not os.path.isdir('C:\\ProgramData\\Sublime Text 3\\')):
                os.makedirs('C:\\ProgramData\\Sublime Text 3\\')
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(['line', 'total', 'infolders', 'folders'])
            metafile = open(self.metafilename, 'w')
            metafile.write('0\n0\n')

    def UpdateCSV(self, path, recursive=True, hidden=False, venv=False):
        self.__DataFromCSV()
        self.__AddToTableFromPath(path, recursive, hidden, venv)
        self.__CSVFromData()

    def ClearCSV(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['line', 'total', 'infolders', 'folders'])
            metafile = open(self.metafilename, 'w')
            metafile.write('0\n0')

    def __DataFromCSV(self):
        self.Table = []
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self.Table += [[row['line'], int(row['total']), int(row['infolders']), int(row['folders'])]]
                self.TableRows += 1
        with open(self.metafilename) as metafile:
            lines = metafile.readlines()
        self.totalFiles = int(lines[0])
        self.totalFolders = int(lines[1])

    def __AddToTableFromPath(self, path, recursive=True, hidden=False, venv=False):
        if (recursive):
            for (dirpath, dirnames, filenames) in os.walk(path):
                current_data = []
                current_rows = 0
                total = 0
                checkpy = 0
                for file in filenames:
                    if ((file[-3:] == '.py') and (dirpath.find('\\.') == -1 or hidden) and (
                            (dirpath.find('\\venv\\') == -1 and dirpath[-5:] != '\\venv') or venv)):
                        checkpy = 1
                        f = open(dirpath + '\\' + file)
                        total += 1
                        try:
                            for line1 in f:
                                line = line1[:-1]
                                if (line[0:7] == 'import ' or line[0:5] == 'from '):
                                    if (current_data == []):
                                        current_data = [[line, 1]]
                                        current_rows += 1
                                        continue
                                    l = 0
                                    r = current_rows - 1
                                    m = 0
                                    while (l <= r):
                                        m = (l + r) // 2
                                        if (line < current_data[m][0]):
                                            r = m - 1
                                        elif (line > current_data[m][0]):
                                            l = m + 1
                                        else:
                                            break
                                    if (l <= r):
                                        current_data[m][1] += 1
                                    else:
                                        current_data.insert(l, [line, 1])
                                        current_rows += 1
                        except:
                            pass
                for current in current_data:
                    if (self.Table == []):
                        self.Table = [[current[0], current[1], total, 1]]
                        self.TableRows += 1
                        continue
                    l = 0
                    r = self.TableRows - 1
                    m = 0
                    while (l <= r):
                        m = (l + r) // 2
                        if (current[0] < self.Table[m][0]):
                            r = m - 1
                        elif (current[0] > self.Table[m][0]):
                            l = m + 1
                        else:
                            break
                    if (l <= r):
                        self.Table[m][1] += current[1]
                        self.Table[m][2] += total
                        self.Table[m][3] += 1
                    else:
                        self.Table.insert(l, [current[0], current[1], total, 1])
                        self.TableRows += 1
                if (checkpy):
                    self.totalFiles += total
                    self.totalFolders += 1
        else:
            for (dirpath, dirnames, filenames) in os.walk(path):
                current_data = []
                current_rows = 0
                total = 0
                checkpy = 0
                for file in filenames:
                    if ((file[-3:] == '.py') and (dirpath.find('\\.') == -1 or hidden) and (
                            (dirpath.find('\\venv\\') == -1 and dirpath[-5:] != '\\venv') or venv)):
                        checkpy = 1
                        f = open(dirpath + '\\' + file)
                        total += 1
                        try:
                            for line1 in f:
                                line = line1[:-1]
                                if (line[0:7] == 'import ' or line[0:5] == 'from '):
                                    if (current_data == []):
                                        current_data = [[line, 1]]
                                        current_rows += 1
                                        continue
                                    l = 0
                                    r = current_rows - 1
                                    m = 0
                                    while (l <= r):
                                        m = (l + r) // 2
                                        if (line < current_data[m][0]):
                                            r = m - 1
                                        elif (line > current_data[m][0]):
                                            l = m + 1
                                        else:
                                            break
                                    if (l <= r):
                                        current_data[m][1] += 1
                                    else:
                                        current_data.insert(l, [line, 1])
                                        current_rows += 1
                        except:
                            pass
                for current in current_data:
                    if (self.Table == []):
                        self.Table = [[current[0], current[1], total, 1]]
                        self.TableRows += 1
                        continue
                    l = 0
                    r = self.TableRows - 1
                    m = 0
                    while (l <= r):
                        m = (l + r) // 2
                        if (current[0] < self.Table[m][0]):
                            r = m - 1
                        elif (current[0] > self.Table[m][0]):
                            l = m + 1
                        else:
                            break
                    if (l <= r):
                        self.Table[m][1] += current[1]
                        self.Table[m][2] += total
                        self.Table[m][3] += 1
                    else:
                        self.Table.insert(l, [current[0], current[1], total, 1])
                        self.TableRows += 1
                if (checkpy):
                    self.totalFiles += total
                    self.totalFolders += 1
                break

    def __CSVFromData(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['line', 'total', 'infolders', 'folders'])
            for i in range(self.TableRows):
                writer.writerow(self.Table[i])
        metafile = open(self.metafilename, "w")
        metafile.write(str(self.totalFiles) + '\n' + str(self.totalFolders) + '\n')


class Predictor:
    def __init__(self):
        self.Table = []
        self.TableRows = 0
        self.filename = 'C:\\ProgramData\\Sublime Text 3\\moduledata.csv'
        if (not os.path.isfile(self.filename)):
            if (not os.path.isdir('C:\\ProgramData\\Sublime Text 3\\')):
                os.makedirs('C:\\ProgramData\\Sublime Text 3\\')
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(['line', 'total', 'infolders', 'folders'])
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self.Table += [[row['line'], int(row['total']), int(row['infolders']), int(row['folders'])]]
                self.TableRows += 1


a = CSVReader()
a.ClearCSV()
a.UpdateCSV('B:\\')
