import csv
with open('data.csv'newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    total_marks = 0
    total_marks.entries = len(file_data)
    for marks in file_data:
        total marks += float(marks[1])
        mean = total_marks/total_entries
        print("mean(average) is -->"+str(mean))

import panda as panda
import ploty.express as px

df = pd.read_csv('data.csv')
fig = px.scatter(df,     x = "student no."
                          y = "marks"
                )
                fig.update_layout(shapes = [
                    dict(
                        type = 'line'
                        y0 = mean, y1 = mean
                        x0 = 0, x1 = total_entries
                    )
                ])
                fig.update_yaxes(rangemode = 'tozero')
                fig.show()

                squaring and getting values
                squared_list = []
                for number in data:
                    a = int(number)-mean(data)
                    a = a**2
                    square.list.append(a)
                        