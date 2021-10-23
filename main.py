import dataHandler
fileName = 'data.csv'

inputData = dataHandler.FileHandler(fileName)
inputData.convertTo15m()
print(inputData.rows)