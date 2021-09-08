from tkinter import *
from functools import partial
from resources.config import dict, save_data
from fishing_functionality import start_fishing

def init(root):

    firstColumnText = Label(root, text = "Fishing")
    firstColumnText.grid(row=0, column=0, pady=(3, 0))
    firstColumn = LabelFrame(root)
    firstColumn.grid(row=1, column=0, padx=(10, 0), pady=(0, 5))
    firstColumnFirstRowHeaderText = Label(firstColumn, text = "Rectangle position (px)")
    firstColumnFirstRowHeaderText.grid(row=0, column=0)
    firstColumnFirstRow = LabelFrame(firstColumn)
    firstColumnFirstRow.grid(row=1, column=0, padx=(10))
    firstColumnFirstRowX = Label(firstColumnFirstRow, height=1)
    firstColumnFirstRowX.grid(row=0, column=0, padx=(20,19))
    firstColumnFirstRowXText = Label(firstColumnFirstRowX, text="X:")
    firstColumnFirstRowXText.grid(row=0, column=0, pady=(20, 0))
    firstColumnFirstRowXScale = Scale(firstColumnFirstRowX, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['x'])
    firstColumnFirstRowXScale.grid(row=0, column=1)
    firstColumnFirstRowXEntry = Entry(firstColumnFirstRowX, width=4, textvariable=dict['fishing']['x'])
    firstColumnFirstRowXEntry.grid(row=0, column=2, pady=(20, 0))
    firstColumnFirstRowY = Label(firstColumnFirstRow, height=1)
    firstColumnFirstRowY.grid(row=1, column=0)
    firstColumnFirstRowYText = Label(firstColumnFirstRowY, text="Y:")
    firstColumnFirstRowYText.grid(row=0, column=0, pady=(20, 0))
    firstColumnFirstRowYScale = Scale(firstColumnFirstRowY, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['y'])
    firstColumnFirstRowYScale.grid(row=0, column=1)
    firstColumnFirstRowYEntry = Entry(firstColumnFirstRowY, width=4, textvariable=dict['fishing']['y'])
    firstColumnFirstRowYEntry.grid(row=0, column=2, pady=(20, 0))
    firstColumnSecondRowHeaderText = Label(firstColumn, text = "Rectangle attributes (px)")
    firstColumnSecondRowHeaderText.grid(row=2, column=0)
    firstColumnSecondRow = LabelFrame(firstColumn)
    firstColumnSecondRow.grid(row=3, column=0, padx=(10))
    firstColumnSecondRowX = Label(firstColumnSecondRow, height=1)
    firstColumnSecondRowX.grid(row=0, column=0, padx=(5))
    firstColumnSecondRowXText = Label(firstColumnSecondRowX, text="Width:")
    firstColumnSecondRowXText.grid(row=0, column=0, pady=(20, 0))
    firstColumnSecondRowXScale = Scale(firstColumnSecondRowX, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['width'])
    firstColumnSecondRowXScale.grid(row=0, column=1)
    firstColumnSecondRowXEntry = Entry(firstColumnSecondRowX, width=4, textvariable=dict['fishing']['width'])
    firstColumnSecondRowXEntry.grid(row=0, column=2, pady=(20, 0))
    firstColumnSecondRowY = Label(firstColumnSecondRow, height=1)
    firstColumnSecondRowY.grid(row=1, column=0, padx=(5))
    firstColumnSecondRowYText = Label(firstColumnSecondRowY, text="Height:")
    firstColumnSecondRowYText.grid(row=0, column=0, pady=(20, 0))
    firstColumnSecondRowYScale = Scale(firstColumnSecondRowY, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['height'])
    firstColumnSecondRowYScale.grid(row=0, column=1)
    firstColumnSecondRowYEntry = Entry(firstColumnSecondRowY, width=4, textvariable=dict['fishing']['height'])
    firstColumnSecondRowYEntry.grid(row=0, column=2, pady=(20, 0))
    firstColumnThirdRow = LabelFrame(firstColumn)
    firstColumnThirdRow.grid(row=4, column=0, pady=(5, 0))
    firstColumnThirdRowButton = Button(firstColumnThirdRow, text = "Show rectangle")
    firstColumnThirdRowButton.configure(command = partial(popup_rectangle_window, firstColumnThirdRowButton, dict['fishing']['x'], dict['fishing']['y'], dict['fishing']['width'], dict['fishing']['height']))
    firstColumnThirdRowButton.grid(row=4, column=0, padx=(50, 51), pady=(2, 4))

    secondColumnText = Label(root, text = "Repairing")
    secondColumnText.grid(row=0, column=1, pady=(3, 0))
    secondColumn = LabelFrame(root)
    secondColumn.grid(row=1, column=1, padx=(10, 0), pady=(0, 93))
    secondColumnFirstRowHeaderText = Label(secondColumn, text = "Click position (px)")
    secondColumnFirstRowHeaderText.grid(row=0, column=0)
    secondColumnFirstRow = LabelFrame(secondColumn)
    secondColumnFirstRow.grid(row=1, column=0, padx=(10))
    secondColumnFirstRowX = Label(secondColumnFirstRow, height=1)
    secondColumnFirstRowX.grid(row=0, column=0, padx=(5))
    secondColumnFirstRowXText = Label(secondColumnFirstRowX, text="X:", anchor="s")
    secondColumnFirstRowXText.grid(row=0, column=0, pady=(20, 0))
    secondColumnFirstRowXScale = Scale(secondColumnFirstRowX, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['repairing']['x'])
    secondColumnFirstRowXScale.grid(row=0, column=1)
    secondColumnFirstRowXEntry = Entry(secondColumnFirstRowX, width=4, textvariable=dict['repairing']['x'])
    secondColumnFirstRowXEntry.grid(row=0, column=2, pady=(20, 0))
    secondColumnFirstRowY = Label(secondColumnFirstRow, height=1)
    secondColumnFirstRowY.grid(row=1, column=0)
    secondColumnFirstRowYText = Label(secondColumnFirstRowY, text="Y:")
    secondColumnFirstRowYText.grid(row=0, column=0, pady=(20, 0))
    secondColumnFirstRowYScale = Scale(secondColumnFirstRowY, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['repairing']['y'])
    secondColumnFirstRowYScale.grid(row=0, column=1)
    secondColumnFirstRowYEntry = Entry(secondColumnFirstRowY, width=4, textvariable=dict['repairing']['y'])
    secondColumnFirstRowYEntry.grid(row=0, column=2, pady=(20, 0))
    secondColumnSecondRow = LabelFrame(secondColumn)
    secondColumnSecondRow.grid(row=3, column=0)
    secondColumnSecondRowCheckText = Label(secondColumnSecondRow, text="Enable repairs:")
    secondColumnSecondRowCheckText.grid(row=0, column=0, padx=(0, 37))
    secondColumnSecondRowCheckButton = Checkbutton(secondColumnSecondRow)
    secondColumnSecondRowCheckButton.grid(row=0, column=1, padx=(0, 17))
    secondColumnThirdRow = LabelFrame(secondColumn)
    secondColumnThirdRow.grid(row=4, column=0, pady=(3, 0))
    secondColumnSecondRowButton = Button(secondColumnThirdRow, text = "Show repair position")
    secondColumnSecondRowButton.configure(command = partial(popup_rectangle_window, secondColumnSecondRowButton, dict['repairing']['x'], dict['repairing']['y'], dict['repairing']['length'], dict['repairing']['length']))
    secondColumnSecondRowButton.grid(row=0, column=0, padx=(22, 23), pady=(2, 4))

    secondRow = LabelFrame(root)
    secondRow.grid(row=3, columnspan=2, padx=(10, 0), pady=(0, 5))
    secondRowButton = Button(secondRow, text = "Start fishing", font=18)
    secondRowButton.configure(command = partial(start_fishing, root, secondRowButton))
    secondRowButton.grid(row=0, column=0)

def popup_rectangle_window(button, x, y, width, height):
    window = Toplevel()
    window.resizable(False, False)
    window.attributes('-fullscreen', True)
    window.wm_attributes('-transparentcolor', window['bg'])
    canvas = Canvas(window, width=10000, height=10000)
    canvas.create_rectangle(x.get(), y.get(), x.get()+width.get(), y.get()+height.get(), fill="green")
    canvas.pack()
    button.configure(command = partial(destroy_window, window, button, x, y, width, height))


def destroy_window(window, button, x, y, width, height):
    window.destroy()
    button.configure(command = partial(popup_rectangle_window, button, x,y,width,height))

def on_closing(root):
    save_data()
    root.destroy()
