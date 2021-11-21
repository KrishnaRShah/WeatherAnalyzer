import TemperatureData
import FileIO
import numpy as np

class WeatherAnalyzer:
    def __init__(self):
        self.dataTable = FileIO.FileIO().dataTable
        self.tempData = []
        for i in range(len(self.dataTable)):
            self.tempData.append(TemperatureData.TemperatureData(i, self.dataTable))

    def getMinTemp(self):
        MINTemp = 600
        for i in range(len(self.tempData)):
            if self.tempData[i].minTemp<MINTemp:
                MINTemp = self.tempData[i].minTemp
        return MINTemp
    def getMaxTemp(self):
        MAXTemp = -600
        for i in range(len(self.tempData)):
            if self.tempData[i].maxTemp>MAXTemp:
                MAXTemp = self.tempData[i].maxTemp
        return MAXTemp

    def MinTempAnnually(self):
        MinTempAnn = []
        for i in range(0, len(self.tempData),12):
            MinAnnual = []
            MinAnnual.append(self.tempData[i].date.year)
            Min = 100
            for j in range(11 or 12):
                try:
                    if self.tempData[i+j].minTemp < Min:
                        Min = self.tempData[i+j].minTemp
                except IndexError:
                    return MinTempAnn
            MinAnnual.append(Min)
            MinTempAnn.append(MinAnnual)
        return MinTempAnn
    
    def MaxTempAnnually(self):
        MaxTempAnn = []
        for i in range(0, len(self.tempData),12):
            MaxAnnual = []
            MaxAnnual.append(self.tempData[i].date.year)
            Max = -100
            for j in range(11 or 12):
                try:
                    if self.tempData[i+j].maxTemp > Max:
                        Max = self.tempData[i+j].maxTemp
                except IndexError:
                    return MaxTempAnn
            MaxAnnual.append(Max)
            MaxTempAnn.append(MaxAnnual)
        return MaxTempAnn

    def AvgSnowFallAnnually(self):
        annualAvg = []
        for i in range(0, len(self.tempData),12):
            yearAvg = []
            yearSum = []
            TotalSum = 0
            yearAvg.append(self.tempData[i].date.year)
            if i == 348:
                try:
                    for j in range(11):
                        yearSum.append(self.tempData[i + j].snowfall)
                        TotalSum += self.tempData[i + j].snowfall
                    Divider = int(len(yearSum))
                    yearAvg.append(TotalSum/Divider)
                except IndexError:
                    return annualAvg
            else:
                try:
                    for j in range(12):
                        yearSum.append(self.tempData[i + j].snowfall)
                        TotalSum += self.tempData[i + j].snowfall
                    Divider = int(len(yearSum))
                    yearAvg.append(TotalSum/Divider)
                except IndexError:
                    return annualAvg
            annualAvg.append(yearAvg)
        return annualAvg
    
    def AvgTempAnnually(self):
        annualAvg = []
        for i in range(0, len(self.tempData), 12):
            yearAvg = []
            yearSum = []
            TotalSum = 0
            yearAvg.append(self.tempData[i].date.year)
            if i == 348:
                try:
                    for j in range(11):
                        yearSum.append((self.tempData[i + j].maxTemp + self.tempData[i + j].minTemp)/2)
                        TotalSum += ((self.tempData[i + j].maxTemp + self.tempData[i + j].minTemp)/2)
                    Divider = int(len(yearSum))
                    yearAvg.append(TotalSum/Divider)
                except IndexError:
                    return annualAvg
            else:
                try:
                    for j in range(12):
                        yearSum.append((self.tempData[i + j].maxTemp + self.tempData[i + j].minTemp)/2)
                        TotalSum += ((self.tempData[i + j].maxTemp + self.tempData[i + j].minTemp)/2)
                    Divider = int(len(yearSum))
                    yearAvg.append(TotalSum/Divider)
                except IndexError:
                    return annualAvg
            annualAvg.append(yearAvg)
        return annualAvg


    
