import csv
import os
import sublime
import sublime_plugin


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
        self.finalTable = []
        self.finalRows = 0
        self.coefTable = []
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
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self.Table += [[row['line'], int(row['total']), int(row['infolders']), int(row['folders'])]]
                self.TableRows += 1
            with open(self.metafilename) as metafile:
                lines = metafile.readlines()
            self.totalFiles = int(lines[0])
            self.totalFolders = int(lines[1])

    def Ranging(self):
        self.__featureengineering()
        self.__coefselection()
        return self.finalTable

    def __featureengineering(self):
        for row in self.Table:
            self.coefTable += [
                [row[0], row[1] / self.totalFiles, row[3] / self.totalFolders, row[1] / row[2], (1 - row[3] / row[1])]]
        self.Table = []

    def __coefselection(self):
        check = 0
        imports = []
        import_rows = 0
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            for file in filenames:
                if ((file[-3:] == '.py') and (file != os.path.basename(__file__))):
                    f = open(dirpath + '\\' + file)
                    try:
                        for line1 in f:
                            line = line1[:-1]
                            if (line[0:7] == 'import ' or line[0:5] == 'from '):
                                check = 1
                                if (imports == []):
                                    imports = [line]
                                    import_rows += 1
                                    continue
                                l = 0
                                r = import_rows - 1
                                m = 0
                                while (l <= r):
                                    m = (l + r) // 2
                                    if (line < imports[m]):
                                        r = m - 1
                                    elif (line > imports[m]):
                                        l = m + 1
                                    else:
                                        break
                                if (l <= r):
                                    continue
                                else:
                                    imports.insert(l, line)
                                    import_rows += 1
                    except:
                        check = 0
            break
        if (check):
            for row in self.coefTable:
                l = 0
                r = import_rows - 1
                m = 0
                inFolder = False
                while (l <= r):
                    m = (l + r) // 2
                    if (row[0] < imports[m]):
                        r = m - 1
                    elif (row[0] > imports[m]):
                        l = m + 1
                    else:
                        inFolder = True
                        break
                if (inFolder):
                    score = (row[1] + row[2] + 6 * row[3] + 2 * row[4]) / 10
                    if (self.finalTable == []):
                        self.finalTable = [[row[0], score]]
                        self.finalRows += 1
                        continue
                    l = 0
                    r = self.finalRows - 1
                    m = 0
                    while (l <= r):
                        m = (l + r) // 2
                        if (score < self.finalTable[m][1]):
                            r = m - 1
                        else:
                            l = m + 1
                    self.finalTable.insert(l, [row[0], score])
                    self.finalRows += 1
                else:
                    score = (5 * row[1] + 3 * row[2] + row[3] + row[4]) / 10
                    if (self.finalTable == []):
                        self.finalTable = [[row[0], score]]
                        self.finalRows += 1
                        continue
                    l = 0
                    r = self.finalRows - 1
                    m = 0
                    while (l <= r):
                        m = (l + r) // 2
                        if (score < self.finalTable[m][1]):
                            r = m - 1
                        else:
                            l = m + 1
                    self.finalTable.insert(l, [row[0], score])
                    self.finalRows += 1
        else:
            for row in self.coefTable:
                score = (4 * row[1] + 4 * row[2] + row[3] + row[4]) / 10
                if (self.finalTable == []):
                    self.finalTable = [[row[0], score]]
                    self.finalRows += 1
                    continue
                l = 0
                r = self.finalRows - 1
                m = 0
                while (l <= r):
                    m = (l + r) // 2
                    if (score < self.finalTable[m][1]):
                        r = m - 1
                    else:
                        l = m + 1
                self.finalTable.insert(l, [row[0], score])
                self.finalRows += 1
        self.coefTable = []


class UpdateCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.view = None
        self.input_dir = ''
        self.recursive = 'yes'
        self.hidden = 'no'
        self.venv = 'no'
        self.window.show_input_panel('Enter directory name', '', self.on_done1, None, None)

    def on_done1(self, input_dir):
        self.input_dir = input_dir
        self.window.show_input_panel('Recursive?', 'yes', self.on_done2, None, None)

    def on_done2(self, recursive):
        self.recursive = recursive
        self.window.show_input_panel('Include hidden folders (starting with .)?', 'no', self.on_done3, None, None)

    def on_done3(self, hidden):
        self.hidden = hidden
        self.window.show_input_panel('Include venv folders?', 'no', self.on_done4, None, None)

    def on_done4(self, venv):
        self.venv = venv
        a = CSVReader()
        a.UpdateCSV(self.input_dir, self.recursive == 'yes', self.hidden != 'no', self.venv != 'no')
        del a


class ClearCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.answer = 'yes'
        self.window.show_input_panel('Clear all data?', 'yes', self.on_done, None, None)

    def on_done(self, answer):
        self.answer = answer
        if (answer == 'yes'):
            a = CSVReader()
            a.ClearCSV()
            del a


class AutoimportCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.notfirst = False
        a = Predictor()
        self.list_of = a.Ranging()
        self.list_of = [row[0] for row in self.list_of]
        self.list_of.reverse()
        self.window.show_quick_panel(self.list_of, 0, 0, 0, self.on_highlighted)

    def on_highlighted(self, answer):
        if (self.notfirst):
            self.window.active_view().run_command('import', {'text': self.list_of[answer]})
        self.notfirst = True


class ImportCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.insert(edit, 0, text + '\n')
