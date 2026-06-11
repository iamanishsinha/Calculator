import customtkinter as ctk
from math import sqrt

# APP CONFIG 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

WIDTH = 420
HEIGHT = 630

app.geometry(f"{WIDTH}x{HEIGHT}")
app.minsize(WIDTH, HEIGHT)

app.title("Calculator")

# Smooth scaling

ctk.set_widget_scaling(1.0)
ctk.set_window_scaling(1.0)

#COLORS 
BG_COLOR = "#eaf0d6"
BUTTON_COLOR = "#ffffa9"
OPERATOR_COLOR = "#e5e5e5"
HOVER_COLOR = "#dcdcdc"
EQUAL_COLOR = "#7d7d7d"
CLEAR_COLOR = "#b72121"
TEXT_COLOR = "#111111"
WHITE = "#e7ecc4"

# VARIABLES

expression = ""
display_var = ctk.StringVar(value="0")

#MAIN FRAME

main_frame = ctk.CTkFrame(
    app,
     fg_color=BG_COLOR,
     corner_radius=0
)

main_frame.pack(fill="both", expand=True)

#DISPLAY

display_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent",
    height=120
)

display_frame.pack(
    fill="x",
    padx=20,
    pady=(20, 10)
)

display_frame.pack_propagate(False)

display = ctk.CTkEntry(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 42),
    justify="right",
    fg_color="#ffffff",
    text_color=TEXT_COLOR,
    border_width=0,
    corner_radius=20,
    height=90
)

display.pack(fill="both", expand=True)

#FUNCTIONS
def update_display(value):
    display_var.set(value)
        
 
  
def press(value):
    global expression
               
    if display_var.get() ==  "0":
        expression = str(value)
    else:
         expression  +=  str(value)
  
    update_display(expression)

   
def clear():
    global expression

    expression = ""
    update_display("0")


def calculate(event=None):
    global expression

    try:
        result = eval(expression)

        if isinstance(result, float):
            result = round(result, 8)

        expression = str(result)
        update_display(expression)

    except:
        expression = ""
        update_display("Error")


def percentage():
    global expression

    try:
        result = eval(expression) / 100
        result = round(result, 8)

        expression = str(result)

        update_display(expression)

    except:
        expression = ""
        update_display("Error")


def square_root():
    global expression

    try:
        result = sqrt(float(eval(expression)))

        result = round(result, 8)
        expression = str(result)
        update_display(expression)

    except:
        expression = ""
        update_display("Error")


#BUTTON FRAME 

button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

button_frame.pack(
    fill="both",
    expand=True,
    padx=18,
    pady=(0, 18)
)


# Responsive grid
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)




#BUTTON CREATOR 

BUTTON_FONT = ("Segoe UI", 28)


def create_button(
      text,
      row,
       col,
        command,
        fg=BUTTON_COLOR,
         hover=HOVER_COLOR,
         text_color=TEXT_COLOR,
        colspan=1
):

    button = ctk.CTkButton(
        button_frame,
        text=text,
        command=command,
        font=BUTTON_FONT,
         fg_color=fg,
        hover_color=hover,
          text_color=text_color,
         corner_radius=18,
         border_width=0
     )

    button.grid(
     row=row,
        column=col,
         columnspan=colspan,
     sticky="nsew",
         padx=5,
         pady=5
 )

    return button


#BUTTONS    
   
buttons =   [
     ("7", 0, 0),
     ("8", 0, 1),
     ("9", 0, 2),
     ("÷", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("×", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("%", 3, 2),
    ("+", 3, 3),
]

for (text, row, col) in buttons:

    if text == "÷":

        create_button(
            text, 
              row, 
             col,
            lambda: press("/"),
            fg=OPERATOR_COLOR
        )

    elif text == "×":

        create_button(
            text,
             row,  
              col,
            lambda: press("*"),
            fg=OPERATOR_COLOR
        )

    elif text in ["+", "-", "%"]:

        if text == "%":

            create_button(
                text,
            row,
             col,
                percentage,
                fg=OPERATOR_COLOR
            )

        else:

            create_button(
                text,
                row,
                col,
                lambda t=text: press(t),
                fg=OPERATOR_COLOR
            )

    else:

        create_button(
            text,
            row,
            col,
            lambda t=text: press(t)
        )

#  LAST ROW 

create_button(
    "√",
    4,
    0,
    square_root,
    fg=OPERATOR_COLOR
)
    
create_button(
    "C",
    4,
    1,
    clear,
    fg=CLEAR_COLOR,
    hover="#ff4444",
    text_color=WHITE
)
          
create_button(
    "=",
    4,
    2,
    calculate,
    fg=EQUAL_COLOR,
    hover="#6b6b6b",
    text_color=WHITE,
    colspan=2
) 
 
#KEYBOARD SUPPORT     
    
def key_press(event):

    key = event.keysym

    #Numbers 
    if key in [str(i) for i in range(10)]:
        press(key)

    # Operators  
    elif key in ["plus", "KP_Add"]:
        press("+")

    elif key in ["minus", "KP_Subtract"]:
        press("-")

    elif key in ["asterisk", "KP_Multiply"]:
        press("*")

    elif key in ["slash", "KP_Divide"]:
        press("/")

    #Decimal
    elif key in ["period", "KP_Decimal"]:
        press(".")

    #Enter
    elif key in ["Return", "KP_Enter"]:
        calculate()

    #  Backspace 
    elif key == "BackSpace":

        global expression

        expression = expression[:-1]

        if expression == "":
            update_display("0")
        else:
            update_display(expression)

    # Escape 
    elif key == "Escape":
        clear()


app.bind("<Key>", key_press)

# START "Run to Start the Calculator"

app.mainloop()
