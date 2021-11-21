import WeatherAnalyzer
import numpy as np
import matplotlib.pyplot as pyplot
import TemperatureData
import FileIO
import Date

WeatherAnal = WeatherAnalyzer.WeatherAnalyzer()

class Chart:

    def __init__(self):
        self.dataTable = FileIO.FileIO().dataTable
        self.tempData = []
        for i in range(len(self.dataTable)):
            self.tempData.append(TemperatureData.TemperatureData(i, self.dataTable))

    def drawLineChart(self,x,y,title,ylabel,xlabel):
            fig = pyplot.figure()
            pyplot.title(title)
            pyplot.ylabel(ylabel)
            pyplot.xlabel(xlabel)
            pyplot.plot(x,y, marker = 'o')
            pyplot.show()
    
    def drawBarChart(self,x,y,title,xlabel,ylabel):
            objects = x
            y_pos = np.arange(len(objects))
            performance = y
            pyplot.bar(y_pos, performance, align='center', alpha=0.5)
            pyplot.xticks(y_pos, objects, rotation = "90")
            pyplot.ylabel(ylabel)
            pyplot.xlabel(xlabel)
            pyplot.title(title)
            pyplot.show()



        



    

    



    
        
    
            
        

    
        

    


