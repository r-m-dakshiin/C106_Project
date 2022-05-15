import csv
import plotly.express as px
import numpy as np

def plotfigure(data_path):
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

with open("Student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.bar(df, x="Marks In Percentage", y="Days Present", color="Roll No")
    fig.show()
def getDataSource(data_path):
    Student_marks = []
    Days_present = []
    with open("Student Marks vs Days Present.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Student_marks.append(float(row["Roll No"]))
            Days_present.append(float(row["Marks In Percentage"]))
    return{"x" : Student_marks, "y" : Days_present}

def findCorrelation(data_source):

    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Marks in percentage and Days Present : ", correlation[0,1])
    
plotfigure("a")