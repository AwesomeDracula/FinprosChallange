import csv


class FileHandler:
    def __init__(self, filename):
        self.fields = []
        self.rows = []
        with open(filename, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            self.fields = next(csvReader)
            for row in csvReader:
                self.rows.append(row)

    def convertTo15m(self):
        convertedRows = []
        idx = 0
        while idx < len(self.rows) - 14:
            if self.rows[idx][0].split()[1] == '11:30' \
                    or self.rows[idx][0].split()[1] == '14:30' \
                    or self.rows[idx][0].split()[1] == '14:45':
                convertedRows.append(self.rows[idx])
                idx += 1
                continue
            newTime = self.rows[idx][0]
            newOpen = self.rows[idx][1]
            newHigh = 0
            newLow = 2000
            newClose = self.rows[idx+14][4]
            newVolume = 0
            for row in self.rows[idx:idx+15]:
                if float(row[2]) > newHigh:
                    newHigh = float(row[2])
                if float(row[3]) < newLow:
                    newLow = float(row[3])
                newVolume += float(row[5])
            convertedRows.append([newTime, newOpen, newHigh, newLow, newClose, newVolume])
            idx += 15
        self.rows = convertedRows

