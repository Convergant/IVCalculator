# This is a program designed to provide a user interface that calculates the IVs of a Pokemon,
# as well as providing how many different kinds of experience candy are required to do so, if desired.

from imports import *
from EXPCalculator import *
from data import *


class TextBox:
    def __init__(self, row, column, root, default="", label_text="", label_right=True, width=15, height=1, rowspan=1, columnspan=1, bg="light grey",
                 label_width=5, anchor="center"):
        """
        A class for a box that displays text and cannot be edited by the user, implementing tkinter's Text class.
        :param row: The row to place the text box on.
        :param column: The column to place the text box at.
        :param root: The master object of the text box.
        :param default: The default text to be displayed.
        :param label_text: The text to display as a label for the text box, default is no text.
        :param label_right: Whether the label should be left or right of the text box. Default is to the right.
        :param width: The width of the box. Default is 15.
        :param height: The height of the box. Default is 1.
        :param rowspan: How many rows the box takes up. Default is 1.
        :param columnspan: How many rows the box takes up. Default is 1.
        :param bg: The background colour of the text box. Default is light grey.
        """
        self.__box = Text(root, width=width, height=height, bg=bg)
        self.__box.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        self.__box.insert(END, default)
        self.__box.config(state=DISABLED)

        if label_text:
            self.__label = Label(root, text=label_text, width=label_width, anchor=anchor)
            self.__label.grid(row=row, column=column + (2 * label_right - 1))

    def get(self):
        self.__box.get("1.0", END)

    def set(self, text):
        self.__box.config(state=NORMAL)
        self.clear()
        self.__box.insert(END, text)
        self.__box.config(state=DISABLED)

    def clear(self):
        self.__box.delete("1.0", END)


class DropDown:
    def __init__(self, root, default, values, row=0, column=0, label_text="", label_right=True, command=None, width=25):
        """
        Class to display a drop-down menu using tkinter.
        :param root: The master object to place the dropdown on.
        :param default: The default value of the dropdown.
        :param values: The list of values to select from.
        :param row: The row to place the dropdown on.
        :param column: The column to place the dropdown at.
        :param label_text: The text to display as a label for the dropown, default is no text.
        :param label_right: Whether to display the label to the left or right of the dropdown.
        :param command: The callback command of the dropdown, which is ran when an item is selected. Default is no command.
        """
        self.default = default
        self.values = values

        if not default in values:
            self.values = [default] + self.values

        box = ttk.Combobox(root, values=self.values, width=width)
        box.bind("<<ComboboxSelected>>", command)
        box.set(value=default)
        box.grid(row=row, column=column)
        box.config(width=15)
        self.box = box

        offset = 2*label_right - 1
        label = Label(root, text=label_text)
        label.grid(row=row, column=column+offset)
        self.label = label

    def get(self):
        return self.box.get()

    def set(self, index):
        self.box.current(index)

    def update_values(self, new_values):
        self.values = new_values
        self.box.config(values=self.values)


class StatBox(IntegerInputBox):
    def __init__(self, row, column, stat_name, master, error_label=None, name=""):
        self.__frame = Frame(master)
        self.__frame.grid(row=row, column=column)
        super().__init__(1, 1, self.__frame, input_fg="black", input_bg="white", label_fg="black",
                         label_bg="gray95", label_right=False, input_width=4, error_label=error_label,
                         label_text="", name=name, label_width=0)

        self.__clicked = StringVar()
        self.__clicked.set("")
        self.__judge_eval = AutocompleteCombobox(self.__frame, textvariable=self.__clicked,
                                                 values=["", "No Good", "Decent", "Pretty Good", "Very Good", "Fantastic", "Best"], width=18)
        self.__judge_eval.grid(row=1, column=2)
        self.__judge_eval.set_completion_list(self.__judge_eval["values"])
        self.__stat_label = Label(master, text=stat_name, anchor="w", width=5)
        self.__stat_label.grid(row=row, column=column-1)
        self.__ev_box = IntegerInputBox(1, 3, self.__frame, input_fg="black", input_bg="white", label_fg="black", label_bg="gray95",
                                        error_label=error_label, default=0, min=0, max=252, input_width=6, label_text="", name=name + " EV")

    def get_judge_eval(self):
        return self.__judge_eval.get()

    def get_evs(self):
        return self.__ev_box.get()


class IVBoxes:
    def __init__(self, row, column, master, stat_name, range=[0, 31], width=4):
        self.__frame = Frame(master)
        self.__frame.grid(row=row, column=column)
        self.__min_box = TextBox(0, 1, self.__frame, str(min(range)), label_text=stat_name, width=width, label_right=False, anchor="w", label_width=5)
        self.__max_box = TextBox(0, 3, self.__frame, str(max(range)), width=width, label_text="-", label_right=False)

    def set_range(self, range):
        self.__min_box.set(str(min(range)))
        self.__max_box.set(str(max(range)))


def display_ui():
    input_label = Label(root, text="Pokemon Input")
    input_label.place(x=0, y=0)

    results_label = Label(root, text="Results")
    results_label.place(x=282, y=0)

    candies_label = Label(root, text="Candies")
    candies_label.place(x=450, y=0)

    results_frame = Frame(root, bg="gray95", highlightbackground="grey80", highlightcolor="gray80", highlightthickness=1)
    results_frame.place(x=282, y=20)

    pokemon_frame = Frame(root, bg="gray95", highlightbackground="grey80", highlightcolor="gray80", highlightthickness=1)
    pokemon_frame.place(x=0, y=20)


    error_label = Label(pokemon_frame, text="")
    error_label.grid(row=11, column=1)

    # The pokemon field should have the first Pokémon, alphabetically, auto-selected.
    clicked = StringVar()
    clicked.set(list(names)[0])

    clicked_2 = StringVar()
    clicked_2.set(Nature.Adamant.text())

    # Create the pokemon field; its values are the list of keys for exp_groups_data,
    # and its position is row 0 and column 1.
    pokemon = AutocompleteCombobox(pokemon_frame, textvariable=clicked, values=names, width=20)
    pokemon.grid(row=0, column=1, columnspan=1)
    pokemon.set_completion_list(names)

    level_input = IntegerInputBox(1, 1, pokemon_frame, min=1, max=100,
                                  label_text="Level", label_bg="gray95", label_fg="black", input_bg="white",
                                  input_fg="black", label_right=False, input_width=23, justify=LEFT,
                                  error_label=error_label)

    nature_box = AutocompleteCombobox(pokemon_frame, textvariable=clicked_2, values=[c.text() for c in Nature], width=20)
    nature_box.grid(row=2, column=1, columnspan=1)
    nature_box.set_completion_list([c.text() for c in Nature])

    nature_label = Label(pokemon_frame, text="Nature")
    nature_label.grid(row=2, column=0)

    pokemon_label = Label(pokemon_frame, text="Pokemon")
    pokemon_label.grid(row=0, column=0)

    headings = Label(pokemon_frame, text="Stat \t Judge Rating \t EVs")
    headings.grid(row=3, column=1)

    hp_box = StatBox(4, 1, "HP", pokemon_frame, error_label=error_label, name="HP")
    atk_box = StatBox(5, 1, "Atk", pokemon_frame, error_label=error_label, name="Atk")
    def_box = StatBox(6, 1, "Def", pokemon_frame, error_label=error_label, name="Def")
    spatk_box = StatBox(7, 1, "SpAtk", pokemon_frame, error_label=error_label, name="SpAtk")
    spdef_box = StatBox(8, 1, "SpDef", pokemon_frame, error_label=error_label, name="SpDef")
    speed_box = StatBox(9, 1, "Speed", pokemon_frame, error_label=error_label, name="Speed")

    stats_boxes = [hp_box, atk_box, def_box, spatk_box, spdef_box, speed_box]

    next_level_label = Label(results_frame, text="\n"*4)
    next_level_label.grid(row=0, column=0)

    hp_iv_boxes = IVBoxes(1, 0, results_frame, "HP")
    atk_iv_boxes = IVBoxes(2, 0, results_frame, "Atk")
    def_iv_boxes = IVBoxes(3, 0, results_frame, "Def")
    spatk_iv_boxes = IVBoxes(4, 0, results_frame, "SpAtk")
    spdef_iv_boxes = IVBoxes(5, 0, results_frame, "SpDef")
    speed_iv_boxes = IVBoxes(6, 0, results_frame, "Speed")

    iv_boxes = [hp_iv_boxes, atk_iv_boxes, def_iv_boxes, spatk_iv_boxes, spdef_iv_boxes, speed_iv_boxes]

    results_whitespace = Label(results_frame, text="\n\n")
    results_whitespace.grid(row=7, column=0)

    old_ranges = [[0, 31]]*6

    candy_master = Frame(root, bg="gray95", highlightbackground="grey80", highlightcolor="gray80", highlightthickness=1)
    candy_master.place(x=450, y=20)

    candy_input_frame = Frame(candy_master)
    candy_input_frame.grid(row=0, column=0)

    candy_output_frame = Frame(candy_master)
    candy_output_frame.grid(row=1, column=0)

    candy_buttons_frame = Frame(candy_master)
    candy_buttons_frame.grid(row=2, column=0)

    init_level_box = IntegerInputBox(0, 0, candy_input_frame, min=0, max=100, input_fg="black", input_bg="white",
                                     label_text="Initial Level", label_fg="black", label_bg="gray95", label_width=20,
                                     anchor="w", input_width=20, name="Initial Level")

    final_level_box = IntegerInputBox(1, 0, candy_input_frame, min=0, max=100, input_fg="black", input_bg="white",
                                     label_text="Final Level", label_fg="black", label_bg="gray95", label_width=20,
                                      anchor="w", input_width=20, name="Final Level")

    exp_next_box = IntegerInputBox(2, 0, candy_input_frame, min=0, input_fg="black", input_bg="white",
                                     label_text="EXP to Level Up", label_fg="black", label_bg="gray95", label_width=20,
                                   anchor="w", input_width=20, name="EXP to Level Up", default=0)

    candy_boxes = []

    for counter, candy in enumerate(EXPCandy, 3):
        this_box = EXPCandyBox(counter, 0, candy_output_frame, candy, field_width=10, label_width=20, anchor="w",
                               field_bg="white", field_fg="black", label_bg="gray95", label_fg="black", label_text="Number of " + candy.name + " Candies")

        candy_boxes.append(this_box)

    label_below = Label(candy_master, text="    \n")
    label_below.grid(row=3, column=0)

    excess_xp = []
    exp_group = exp_groups_data.get(pokemon.get().split("-")[0])

    def clear_iv_calculator(*args):
        print("resetting calculator")
        for i in range(len(old_ranges)):
            old_ranges[i] = [0, 31]

    pokemon.bind("<<ComboboxSelected>>", clear_iv_calculator)
    clicked.trace("w", clear_iv_calculator)

    def display_candies(displaying=True):
        """ Display the number of each type of candy.

        :param displaying: Whether the method will actually display, or just return the excess EXP generated.
        :return excess_exp: The excess experience generated by using the candies calculated. """

        # Get the initial and final levels.
        initial_level = init_level_box.get()
        final_level = final_level_box.get()
        exp_group = exp_groups_data.get(pokemon.get())

        # DIsplay and error message if the final level is not greater than the initial level.
        if final_level <= initial_level:
            label_below.config(text="The final level must be\ngreater than the initial level.")
            return

        # Get the EXP to the next level.
        exp_next_level = exp_next_box.get()

        if exp_next_level is None or exp_next_level == 0:
            exp_next_level = exp_group.total_exp(initial_level + 1) - exp_group.total_exp(initial_level)

        # If the input has passed all the test, clear the error message and display the candies.
        if initial_level and final_level and exp_next_level:
            # Clear the error message.
            label_below.config(text="")

            # Get this Pokémon and the candies needed from it.
            this_pokemon = Pokemon(exp_next_level, exp_group)
            data = this_pokemon.candies_needed(initial_level, final_level)
            candies = data[0]
            excess_exp = -data[1]

            if displaying:
                label_below.config(text="Excess EXP: " + str(excess_exp))

                # Loop over every candy.
                for i in range(len(candies)):
                    # Set this EXP candy's text box to contain the number of this kind of candy.
                    candy_boxes[i].set_text_field(candies[i])

            excess_xp.append(excess_exp)

    def level_up():
        init_level_box.set(final_level_box.get())
        final_level_box.clear()
        exp_group = exp_groups_data.get(pokemon.get().split("-")[0])
        exp_next_box.set(exp_group.total_exp(init_level_box.get() + 1) - (exp_group.total_exp(init_level_box.get()) + excess_xp[-1]))

    def reset():
        label_below["text"] = "\n"

        for box in candy_boxes:
            box.reset()

        init_level_box.clear()
        final_level_box.clear()
        exp_next_box.clear()

    candy_calc_button = Button(candy_buttons_frame, text="Calculate", command=display_candies)
    candy_calc_button.grid(row=0, column=0)

    candy_level_up_button = Button(candy_buttons_frame, text="Level Up", command=level_up)
    candy_level_up_button.grid(row=0, column=1)

    candy_reset_button = Button(candy_buttons_frame, text="Reset", command=reset)
    candy_reset_button.grid(row=0, column=2)

    def calc():
        level = level_input.get()
        nature = Nature[nature_box.get().split(" (")[0]]
        stats = [c.get() for c in stats_boxes]
        judge_ranges = [judge_map.get(c.get_judge_eval(), [0, 31]) for c in stats_boxes]
        evs = [c.get_evs() for c in stats_boxes]
        for i in range(len(evs)):
            if evs[i] is None:
                evs[i] = 0

        if level is None:
            return

        if sum(evs) > 508:
            error_label["text"] = "Total EVs must\nnot exceed 508"
            return

        if not all([bool(c) for c in stats]):
            return

        nature_list = nature.value
        base = base_stats_data.get(pokemon.get())

        min_stats = [hp(level, base[0], evs[0], 0)]
        max_stats = [hp(level, base[0], evs[0], 31)]

        for i in range(1, 6):
            min_stats.append(other_stat(level, base[i], evs[i], 0, boosted=(nature_list[i] == 1.1), reduced=(nature_list[i] == 0.9)))
            max_stats.append(other_stat(level, base[i], evs[i], 31, boosted=(nature_list[i] == 1.1), reduced=(nature_list[i] == 0.9)))

        if any([(stats[c] < min_stats[c]) or (stats[c] > max_stats[c]) for c in range(6)]):
            error_label["text"] = "One or more stats\nare invalid."
            return

        init_level_box.set(level)
        ranges = calc_iv_range(level, base, stats, evs, nature)

        for counter, this_range in enumerate(ranges):
            this_range = [max(judge_ranges[counter][0], this_range[0], old_ranges[counter][0]),
            min(judge_ranges[counter][1], this_range[1], old_ranges[counter][1])]
            ranges[counter] = this_range
            iv_boxes[counter].set_range(ranges[counter])

        msg = "Level " + str(level) + ": " + ", ".join(["-".join([str(min(c)), str(max(c))]) for c in ranges])
        print(msg)

        level += 1

        min_stats = [hp(level, base[0], evs[0], min(ranges[0]))]
        max_stats = [hp(level, base[0], evs[0], max(ranges[0]))]

        for i in range(1, 6):
            min_stats.append(other_stat(level, base[i], evs[i], min(ranges[i])))
        max_stats.append(other_stat(level, base[i], evs[i], max(ranges[i])))

        while not all([min(c) == max(c) for c in old_ranges]) and min_stats == max_stats and level < 100:
            level += 1

            min_stats = [hp(level, base[0], evs[0], min(ranges[0]))]
            max_stats = [hp(level, base[0], evs[0], max(ranges[0]))]

            for i in range(1, 6):
                min_stats.append(other_stat(level, base[i], evs[i], min(ranges[i])))
                max_stats.append(other_stat(level, base[i], evs[i], max(ranges[i])))

        for box in stats_boxes:
            box.clear()

        for i in range(len(old_ranges)):
            old_ranges[i] = ranges[i]

        if not all([min(c) == max(c) for c in old_ranges]):
            level_input.set(level)
            next_level_label["text"] = "Recommended Next Level:\n" + str(level) + "\n" * 3
            final_level_box.set(level)
            display_candies()

        else:
            next_level_label["text"] = "IVs found" + "\n" * 4

    calculate_button = Button(pokemon_frame, text="Calculate IVs", command=calc)
    calculate_button.grid(row=10, column=1)

    root.mainloop()


if __name__ == "__main__":
    print("Running main program")

    global root
    root = Tk()

    # photo = PhotoImage(file="background.png")
    # label = Label(image=photo)
    # label.image = photo  # keep a reference!
    # label.place(x=0, y=0, relwidth=1, relheight=1)

    root.title("IV Calculator")
    root.geometry("725x350")

    photo = PhotoImage(file="icon.png")
    root.iconphoto(False, photo)

    display_ui()