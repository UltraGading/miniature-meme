import pandas
import plotly.figure_factory as pff
df = pandas.read_csv('bcnd.csv')
fig = pff.create_distplot([df["Avg Rating"].tolist()], ["ratingers"], show_hist=False)
fig.show()
#test 1
#test 1 successful and complete