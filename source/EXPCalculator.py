# This is a program which calculates what number of each EXP candy in Pokémon Sword and Shield would be required
# to level up a given Pokémon to a specific level.

# Get all of the necessary imports.
from imports import *
from tkinter import *


# This is the class for a particular UI element; a box to display how much of an EXP candy is needed.
# It also has a button which toggles whether the calculation considers those candies,
# so if you don't have enough of that kind of candy. you can exclude it, and a label for the kind of candy.
class EXPCandyBox:
    """ Class which displays a box for the quantity of a kind of candy.

    Includes a button to toggle whether this candy is being considered, and a label describing the candy. """
    def __init__(self, button_row, button_column, master, candy, button_width=5, button_height=1, field_width=25, field_bg="gray45", field_fg="white",
                 label_text="", label_bg="gray35", label_fg="white", button_texts=["ON", "OFF"], button_colours=["blue", "red"], label_width=15, anchor="center"):
        """ Construct a candy box at a position for a candy.

        :param button_row: The row the button inhabits.
        :param button_column: The column the button inhabits.
        :param candy: The candy this box represents.
        :param button_width: The width of the toggle button.
        :param button_height: THe height of the toggle button.
        :param field_width: The width of the display field.
        :param field_bg: The background colour of the display field.
        :param field_fg: The foreground colour of the display field.
        :param label_text: The text displayed by the label.
        :param label_bg: The background colour of the label.
        :param label_fg: The foreground colour of the label.
        :param button_texts: The possible text values the button can have.
        :param button_colours: The possible text colours the button can have. """

        self.__candy = candy
        self.__frame = Frame(master)
        self.__frame.grid(row=button_row, column=button_column)

        # The toggle button is a Button widget, as provided by tkinter, at the location specified
        # with default text "ON", default text colour blue, a width of 5, height of 1,
        # and an on-click command which toggles its colour and text.
        self.__toggle_button = Button(self.__frame, text="ON", command=self.__update_button, fg="blue", width=button_width, height=button_height)
        self.__toggle_button.grid(row=0, column=0)

        # The text field is 1 column ahead of the button.
        self.__text_field = Label(self.__frame, bg=field_bg, fg=field_fg, width=field_width)
        self.__text_field.grid(row=0, column=1, columnspan=1, rowspan=1)

        # The text label is 2 columns ahead of the button.
        self.__text_label = Label(self.__frame, text=label_text, bg=label_bg, fg=label_fg, width=label_width, anchor=anchor)
        self.__text_label.grid(row=0, column=2)

        self.__button_texts = button_texts
        self.__button_colours = button_colours

    def set_text_field(self, value):
        """ Set the value of the text field to a given value. """
        self.__text_field.config(text=str(value))

    def reset(self):
        """ Clear the contents of the text field, and reset the button state. """
        self.__text_field["text"] = ""
        self.__toggle_button["text"] = self.__button_texts[0]
        self.__toggle_button["fg"] = self.__button_colours[0]

    def __update_button(self):
        """ Toggle the text displayed by the button and its colour, and update that EXP candy to toggle whether its
        considered. """

        index = (self.__button_texts.index(self.__toggle_button["text"]) + 1) % len(self.__button_texts)

        self.__toggle_button["text"] = self.__button_texts[index]
        self.__toggle_button["fg"] = self.__button_colours[index]
        EXPCandy[self.__candy.name].value.update()


class IntegerInputBox:
    """ Class for an input box that only accepts integers, using the tkinter library.

    Allows for a minimum, maximum and default value. You can also specify the position, label text, width, column span
    and the error label used."""
    def __init__(self, row, column, master, label_text=None, min=-float("inf"), max=float("inf"), default=None, input_width=25, column_span=1, error_label=None,
                 input_bg="gray45", input_fg="white", label_bg="gray45", label_fg="white", label_right=True, justify=None, name="", anchor="center", label_width=0):
        """  Construct an integer input box at the position specified.

        :param row: The row that the input field will inhabit.
        :param column: The column that the input field will inhabit.
        :param label_text: The text of the label
        :param min: The minimum value the field will accept.
        :param max: The maximum value the field wiill accept.
        :param default: The default value of the field. The field will not display this value.
        :param input_width: The width of the input field.
        :param column_span: The column-span of the input field.
        :param error_label: The error label this object will use to display errors.
        :param input_bg: The background colour of the input field.
        :param input_fg: The foreground colour of the input field.
        :param label_bg: The background colour of the label.
        :param label_fg: The foreground colour of the label. """

        # Assert that the upper bound is greater than the lower bound, and display an error message if not.
        try:
            assert max > min

        except AssertionError:
            msg = "The upper bound must be greater than the lower bound."

            if error_label:
                error_label.config(text=msg)

            else:
                print(msg)

        # The input field is an Entry box (as provided by tkinter), located at the position specified.
        self.__input_field = Entry(master, width=input_width, bg=input_bg, fg=input_fg)
        self.__input_field.grid(row=row, column=column, columnspan=column_span)

        if label_text is not None:
            # The label is 1 column ahead of the input box.
            self.__label = Label(master, text=label_text, bg=label_bg, fg=label_fg, justify=justify, anchor=anchor, width=label_width)
            self.__label.grid(row=row, column=column + 2 * label_right - 1)

        # Set the min, max and default values.
        self.__min = min
        self.__max = max
        self.__default = default

        # Set the error label.
        self.__error_label = error_label
        self.__name = name

    def get(self):
        """ Return the value contained in the input field, if it is valid. """
        value = self.__input_field.get()

        # Call the validation check method, and if it passes, return the value.
        if self.__validate(value):
            return self.__validate(value)

    def set(self, value):
        """ Set the stored value of the input field, if the given value is valid. """
        if self.__validate(value):
            self.clear()
            self.__input_field.insert(0, str(value))

    def clear(self):
        """ Clear the input field. """
        self.__input_field.delete(0, "end")

    def __validate(self, value):
        """ Validate the value contained in this field. """
        try:
            # Assert that the value or the default exists, assert that the value is an integer,
            # assert that if there is a min value, that it is greater than or equal to it,
            # and that if there is a max value, that it is less than or equal to it.
            assert value != "" or self.__default is not None

            if value == "" and self.__default is not None:
                value = self.__default

            elif value != "":
                value = int(value)

            assert int(value) == float(value)

            if self.__min:
                assert self.__min <= value

            if self.__max:
                assert self.__max >= value

        # Catch any assertion errors generated, AKA it didn't pass the validation check.
        except AssertionError:
            # Declare the message initially. Only one error will be shown at a time.
            msg = "Value of " + self.__name + "\n must be "

            # If the value is empty (i.e. none was inputted and there is no default),
            # make the message that the value must be given.
            if not value:
                msg += "given."

            # If the value is not an integer, make the message that it must be an integer.
            elif int(value) != float(value):
                msg += "an integer."

            # If the value is not less than or equal to the max or greater than or equal to the min,
            # make the message that it must be between the two.
            elif self.__min and self.__max:
                msg += "between\n" + str(self.__min) + " and " + str(self.__max) + "."

            # If only the min exists, then say that the value must be greater than or equal to the min.
            elif self.__min:
                msg += "greater than or equal to " + str(self.__min) + "."

            # If only the max exists, then say that the value must be less than or equal to the min.
            else:
                msg += "less than or equal to " + str(self.__max) + "."

            # Display an error message.
            if self.__error_label:
                self.__error_label.config(text=msg)

            else:
                print(msg)

            # Return False, since the validation test was failed.
            return False

        # Return the value, since it is known to be valid.
        return value


