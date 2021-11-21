import WeatherAnalyzer
import Chart
import numpy as np


def main():

    
    WeatherAnal = WeatherAnalyzer.WeatherAnalyzer()
    FullChart = Chart.Chart()

    running = True
    while running:
        print("1- Get Minimum Temperature of 1990-2019")
        print("2- Get Maximum Temperature of 1990-2019")
        print("3- Get Minimum Temperature of 1990-2019 Annually")
        print("4- Get Maximum Temperature of 1990-2019 Annually")
        print("5- Get Average Snowfall between 1990-2019 Annually")
        print("6- Get Average Temperature between 1990-2019 Annually")
        print("7- LineChart Minimum Temperature of 1990-2019 Annually")
        print("8- LineChart Maximum Temperature of 1990-2019 Annually")
        print("9- BarChart Average Snowfall between 1990-2019 Annually")
        print("10- BarChart Average Temperature between 1990-2019 Annually")
        print("11- Exit Program: ")
        
        number = int(input("Please enter a number: "))
        
        if number == 1:
            print(WeatherAnal.getMinTemp())
        elif number == 2:
            print(WeatherAnal.getMaxTemp())
        elif number == 3:
            x = WeatherAnal.MinTempAnnually()
            for i in x:
                for j in i:
                    print(j, end = ' ')
                print()
        elif number == 4:
            x = WeatherAnal.MaxTempAnnually()
            for i in x:
                for j in i:
                    print(j, end = ' ')
                print()
        elif number == 5:
            x = WeatherAnal.AvgSnowFallAnnually()
            for i in x:
                for j in i:
                    print(j, end = ' ')
                print()
        elif number == 6:
            x = WeatherAnal.AvgTempAnnually()
            for i in x:
                for j in i:
                    print(j, end = ' ')
                print()
        elif number == 7:
            data = np.array(WeatherAnal.MinTempAnnually())
            FullChart.drawLineChart(data[:, 0],data[:, 1],"Minimum Temperature of 1990-2019 Annually","Min Temperature(C)","Year")
        elif number == 8:
            data = np.array(WeatherAnal.MaxTempAnnually())
            FullChart.drawLineChart(data[:, 0],data[:, 1],"Maximum Temperature of 1990-2019 Annually","Max Temperature(C)","Year")
        elif number == 9:
            data = np.array(WeatherAnal.AvgSnowFallAnnually())
            FullChart.drawBarChart(data[:, 0],data[:, 1],"Barchart of Average Snowfall between 1990-2019 Annually","Years", "Average Snowfall")
        elif number == 10:
            data = np.array(WeatherAnal.AvgTempAnnually())
            FullChart.drawBarChart(data[:, 0],data[:, 1],"Barchart of Average Temperature between 1990-2019 Annually","Years", "Average Temperature(C)")
        elif number == 11:
            print("Thank you for using my program!")
            running = False
        

        else:
            print("The data type you have selected does not exist")


if __name__ == "__main__":
    main()