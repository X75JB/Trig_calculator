# Trig Calculator
# Jackson Blackman
# 11_07_22

from tkinter import Label, Button, Entry
from math import radians, sin, cos, tan


# Functions
## Calculating ratios
def calculate_ratios(angle):
    try:
        sine_ratio = round(sin(radians(float(angle))), 4)
        cosine_ratio = round(cos(radians(float(angle))), 4)
        tan_ratio = round(tan(radians(float(angle))), 4)

        sine_ratio_output.config(text=sine_ratio)
        cosine_ratio_output.config(text=cosine_ratio)
        tan_ratio_output.config(text=tan_ratio)

    except:
        sine_ratio_output.config(text='Error')
        cosine_ratio_output.config(text='Error')
        tan_ratio_output.config(text='Error')


# Gathering starting values
Label(text='Enter an angle in a right triangle: ').grid(row=0, column=0)
angle_entry = Entry()
angle_entry.grid(row=0, column=1)
angle_entry.focus_set()

## Calculation button
ratio_button = Button(text='Calculate Trig Ratios', command=lambda: calculate_ratios(angle_entry.get()))
ratio_button.grid(row=1, column=0)

# State final ratios
Label(text='The sine ratio is: ').grid(row=2, column=0)
sine_ratio_output = Label()
sine_ratio_output.grid(row=2, column=1)

Label(text='The cosine ratio is: ').grid(row=3, column=0)
cosine_ratio_output = Label()
cosine_ratio_output.grid(row=3, column=1)

Label(text='The tan ratio is: ').grid(row=4, column=0)
tan_ratio_output = Label()
tan_ratio_output.grid(row=4, column=1)
