import csv
import plotly.express as px
import numpy as np

def plotfigure(data_path):
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)


with open('cups of coffee vs hours of sleep.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")
    fig.show()


def getDataSource(data_path):
    Student_marks = []
    Days_present = []
    with open("cups of coffee vs hours of sleep.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Student_marks.append(float(row["week"]))
            Days_present.append(float(row["Coffee in ml"]))
    return{"x" : Student_marks, "y" : Days_present}

def findCorrelation(data_source):

    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Coffee in ml and sleep in hours : ", correlation[0,1])
    
plotfigure("cups of coffee vs hours of sleep.csv")



