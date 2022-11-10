import pandas
from bokeh.plotting import figure, output_file, show
import openpyxl

#feed bokeh plot with pandas csv arrays
df=pandas.read_excel("weatherdata.xlsx")
x=df["Temperature"]/10 #x column
y=df["Pressure"]/10 #y column

p=figure(width=500,height=400, tools='pan')
 
p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature"
p.yaxis.axis_label="Pressure"    
 
p.circle(x,y, size=1, color="navy", alpha=1)
output_file("weatherplot.html")
show(p)
