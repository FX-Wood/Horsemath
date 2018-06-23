#horsemath_calculator.py


import tkinter

master = tkinter.Tk(className=" Horsemath Calculator")

window = tkinter.Frame(master)
window.grid()

party_size = tkinter.IntVar()
party_size.set(1)

party_strength = tkinter.IntVar()
party_strength.set(15)

number_of_horses = tkinter.IntVar()
number_of_horses.set(0)

journey_length = tkinter.IntVar()
journey_length.set(3)

number_of_rations = tkinter.IntVar()
number_of_rations.set(0)

weight_of_rations = tkinter.IntVar()
weight_of_rations.set(0)

carry_weight_remaining = tkinter.IntVar()
carry_weight_remaining.set(0)

quantity_of_feed = tkinter.IntVar()
quantity_of_feed.set(0)

weight_of_feed = tkinter.IntVar()
weight_of_feed.set(0)

def compute_user_journey(self):
    days = journey_length.get()

    people = party_size.get()
    strength = party_strength.get()
    party_capacity = party_strength.get()*15

    rations = people*days
    rations_weight = rations*2

    horses = number_of_horses.get()
    feed = horses*days
    feed_weight = feed*5

    horse_capacity = horses*480

    carry_capacity = horse_capacity + party_capacity

    number_of_rations.set(rations)
    weight_of_rations.set(rations_weight)
    quantity_of_feed.set(feed)
    weight_of_feed.set(feed_weight)
    carry_weight_remaining.set(carry_capacity - rations_weight - feed_weight)

#input rows
party_size_row = 0
party_strength_row = 1
number_of_horses_row = 2
journey_length_row = 3

#output rows
rations_row = 4
weight_of_rations_row = 5
feed_row = 6
weight_of_feed_row = 7
carry_weight_remaining_row = 8

#row for buttons
button_row = 9

party_size_label = tkinter.Label(window, text="Enter number of party members:")
party_size_label.grid(row=party_size_row)

party_size_entry = tkinter.Entry(window, textvariable=party_size)
party_size_entry.grid(row=party_size_row, column=1)
party_size_entry.bind("<Return>", compute_user_journey)


party_strength_label = tkinter.Label(window, text="Enter sum of party strength score")
party_strength_label .grid(row=party_strength_row)

party_strength_entry = tkinter.Entry(window, textvariable=party_strength)
party_strength_entry.grid(row=party_strength_row, column=1)
party_strength_entry.bind("<Return>", compute_user_journey)


number_of_horses_label = tkinter.Label(window, text="Enter number of pack horses")
number_of_horses_label .grid(row=number_of_horses_row)

number_of_horses_entry = tkinter.Entry(window, textvariable=number_of_horses)
number_of_horses_entry.grid(row=number_of_horses_row, column=1)
number_of_horses_entry.bind("<Return>", compute_user_journey)




journey_length_label= tkinter.Label(window, text="Enter journey length in days:")
journey_length_label.grid(row=journey_length_row)

journey_length_entry = tkinter.Entry(window, textvariable=journey_length)
journey_length_entry.grid(row=journey_length_row, column=1)
journey_length_entry.bind("<Return>", compute_user_journey)



rations_label = tkinter.Label(window, text="Necessary rations:")
rations_label.grid(row=rations_row)

rations_variable_label = tkinter.Label(window, textvariable=number_of_rations)
rations_variable_label.grid(row=rations_row, column=1)

weight_of_rations_label = tkinter.Label(window, text="Weight of rations:")
weight_of_rations_label.grid(row=weight_of_rations_row)

weight_of_rations_variable_label = tkinter.Label(window, textvariable=weight_of_rations)
weight_of_rations_variable_label.grid(row=weight_of_rations_row, column=1)

feed_label = tkinter.Label(window, text="Necessary feed:")
feed_label.grid(row=feed_row)

feed_variable_label = tkinter.Label(window, textvariable=quantity_of_feed)
feed_variable_label.grid(row=feed_row, column=1)

weight_of_feed_label = tkinter.Label(window, text="Feed weight:")
weight_of_feed_label.grid(row=weight_of_feed_row)

weight_of_feed_variable_label = tkinter.Label(window, textvariable=weight_of_feed)
weight_of_feed_variable_label.grid(row=weight_of_feed_row, column=1)





carry_weight_remaining_label = tkinter.Label(window, text="Unencumbered weight remaining")
carry_weight_remaining_label.grid(row=carry_weight_remaining_row)

carry_weight_remaining_variable = tkinter.Label(window, textvariable=carry_weight_remaining)
carry_weight_remaining_variable.grid(row=carry_weight_remaining_row, column=1)




compute_button = tkinter.Button(window, text="Compute Journey", relief="groove", width=15)
compute_button.bind("<Button-1>", compute_user_journey)
compute_button.grid(row=button_row)

# class IncludeCoins(tkinter.Tk):

#         def __init__(className=" Coin Calculator"):

#         first_pane = tkinter.PanedWindow()
#         first_pane.pack()

#         second_pane = tkinter.PanedWindow(first_pane, orient="vertical")
#         first_pane.add(second_pane)

#         coin_input_row = 0

#         coins_held_value = tkinter.IntVar()
#         coins_held_value.set(0)

#         coin_input_label = tkinter.Label(first_pane, text="Enter quantity of GP held:")
#         second_pane.add(coin_input_label)

#         coin_input_entry = tkinter.Entry(second_pane, textvariable=coins_held_value)
#         coin_input_entry.bind("<Return>")
#         second_pane.add(coin_input_entry)

# include_coins_button = tkinter.Button(window, text="Include Coins", width=15)
# include_coins_button.bind("<Button-1>", IncludeCoins)
# include_coins_button.grid(row=button_row, column = 1)




master.mainloop()
