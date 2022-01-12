import csv
from os import times
import statistics as st
import pygal as pg
from pandas import Timestamp

#for number 1 of case 4
weekDaysDict = {}
weekEndsDict = {}

file = "newActivity.csv" #csv file where all the NA has been changed to 0 using the solution for case 3

with open(file) as f:
    readCSV = csv.reader(f)
    headerRow = next(readCSV)
    print(headerRow)

    #getting the data
    indexNum = 0
    for rows in readCSV:
        interval = int(rows[2])
        stepsTaken = rows[0]
        Date = Timestamp(rows[1])
        indexNum += 1

        if Date.dayofweek <= 4:
            rows.append("weekdays")
            weekDaysDict.setdefault(interval, [])
            weekDaysDict[interval].append(int(stepsTaken))
        else:
            rows.append("weekend")
            weekEndsDict.setdefault(interval, [])
            weekEndsDict[interval].append(int(stepsTaken))

    weekEndsLi = []
    for day in weekEndsDict.keys():
        weekEndsLi.append(st.mean(weekEndsDict.get(day)))

    weekDaysLi = []
    for day in weekDaysDict.keys():
        weekDaysLi.append(st.mean(weekDaysDict.get(day)))

    histWeekday = pg.Bar()
    histWeekday.title = "Average steps on weekdays"
    histWeekday._x_title = "Date"
    histWeekday._y_title = "Step Frequency"
    histWeekday.add("Averaged number of steps taken", weekDaysLi)
    histWeekday.render_to_file("AverageWeekdayStepsHistogram.svg")
    
    histWeekend = pg.Bar()
    histWeekend.title = "Average steps on weekends"
    histWeekend._x_title = "Date"
    histWeekend._y_title = "Step Frequency"
    histWeekend.add("Averaged number of steps taken", weekEndsLi)
    histWeekend.render_to_file("AverageWeekendStepsHistogram.svg")

