# This is a program which will calculate the IVs of a Pokemon given its stats, level, EVs, and nature.
# It provides the basic logic for the IV calculating section of the UI.

from math import floor
from enum import Enum


stats_names = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]


class Nature(Enum):
    """ Enum for the nature of a Pokemon. Note that duplicate values get collapsed, so
    Bashful is the only neutral nature in the dropdown. """
    Adamant = [1, 1.1, 1, 0.9, 1, 1]
    Bashful = [1] * 6
    Bold = [1, 0.9, 1.1, 1, 1, 1]
    Brave = [1, 1.1, 1, 1, 1, 0.9]
    Calm = [1, 0.9, 1, 1, 1.1, 1]
    Careful = [1, 1, 1, 0.9, 1.1, 1]
    Docile = [1] * 6
    Gentle = [1, 1, 0.9, 1, 1.1, 1]
    Hardy = [1] * 6
    Hasty = [1, 1, 0.9, 1, 1, 1.1]
    Impish = [1, 1, 1.1, 0.9, 1, 1]
    Jolly = [1, 1, 1, 0.9, 1, 1.1]
    Lax = [1, 1, 1.1, 1, 0.9, 1]
    Lonely = [1, 1.1, 0.9, 1, 1, 1]
    Mild = [1, 1, 0.9, 1.1, 1, 1]
    Modest = [1, 0.9, 1, 1.1, 1, 1]
    Naive = [1, 1, 1, 1, 0.9, 1.1]
    Naughty = [1, 1.1, 1, 1, 0.9, 1]
    Quiet = [1, 1, 1, 1.1, 1, 0.9]
    Quirky = [1] * 6
    Rash = [1, 1, 1, 1.1, 0.9, 1]
    Relaxed = [1, 1, 1.1, 1, 1, 0.9]
    Sassy = [1, 1, 1, 1, 1.1, 0.9]
    Serious = [1] * 6
    Timid = [1, 0.9, 1, 1, 1, 1.1]

    def text(self):
        """ Get a string representation of the nature, and return it.

        This is achieved by putting the name, along with the name of the boosted stat with a +, and the reduced stat with a -.
        For example: Nature.Admanant would become Adamant (+Atk,-SpA).
        """
        txt = self.name

        # Only add the details of the boosted and reduced stats if this is not a reducing nature.
        if self.value != [1] * 6:
            boosted_index = self.value.index(1.1)
            reduced_index = self.value.index(0.9)

            txt += " (+" + stats_names[boosted_index] + ",-" + stats_names[reduced_index] + ")"

        return txt


def hp(level, base, ev, iv):
    """ Calculate the HP stat of a Pokemon, and return it.

    The formula can be found at https://bulbapedia.bulbagarden.net/wiki/Statistic#In_Generation_III_onward.
    """
    return floor(level / 100 * (2 * base + iv + floor(ev / 4))) + level + 10


def other_stat(level, base, ev, iv, boosted=False, reduced=False):
    """ Calculate a stat other than HP, and return it.

    The formula can be found at https://bulbapedia.bulbagarden.net/wiki/Statistic#In_Generation_III_onward.
    """
    assert not (boosted and reduced)

    stat = floor(level / 100 * (2 * base + iv + floor(ev / 4))) + 5

    if boosted:
        stat = floor(stat * 1.1)

    elif reduced:
        stat = floor(stat * 0.9)

    return stat


def calc_iv_range(level, base_stats, stats, evs, nature):
    """ Calculate the IV ranges of a Pokemon, and return them.

    Note that this does not take into account any other ranges calculated; it just gives the
    minimum and maximum possible IVs for each stat given the stats at this level.
    """
    ivs = [[0, 31]] * 6
    nature_list = nature.value

    # Loop over every IV range.
    for index, iv_range in enumerate(ivs):
        min, max, min_found, max_found = 0, 31, False, False

        # Loop over every possible ID in this stat.
        for iv in range(32):
            # Calculate the stats for this IV at this level, and the next IV.
            if index != 0:
                this_stat = other_stat(level, base_stats[index], evs[index], iv, boosted=(nature_list[index] == 1.1), reduced=(nature_list[index] == 0.9))
                next_stat = other_stat(level, base_stats[index], evs[index], iv+1, boosted=(nature_list[index] == 1.1), reduced=(nature_list[index] == 0.9))

            else:
                this_stat = hp(level, base_stats[index], evs[index], iv)
                next_stat = hp(level, base_stats[index], evs[index], iv+1)

            # If the stat at this IV is the real stat:
            if this_stat == stats[index]:
                # If this is the first time an IV matches this stat, then it is the minimum possible IV at this level.
                if not min_found:
                    min_found = True
                    min = iv

                # If the stat at the IV above does not match this stat, then it is the
                # maximum possible IV at this level, and the search for the IV range for this stat is done.
                if this_stat != next_stat:
                    max_found = True
                    max = iv
                    break

        # Set this IV range.
        ivs[index] = [min, max]

    # Return the found IV ranges.
    return ivs


def get_ivs(level, base_stats, stats, evs, nature):
    """ Get all of IVs precisely, and return them.

    This method is not used in the main program, however the code there is based off of this,
    and it is arguably more readable than the main code, so its useful to keep it.
    """
    ranges = calc_iv_range(level, base_stats, stats, evs, nature)
    # print(", ".join([display_range(c) for c in ranges]))
    nature_list = nature.value

    # Loop until the level reaches 100, or all of the ranges have the same max and min
    # (i.e., all of the IVs have been found)
    while not all(max(c) == min(c) for c in ranges) and level < 100:
        level += 1

        # Get the minimum and maximum stats at this level
        min_stats = [hp(level, base_stats[0], evs[0], min(ranges[0]))]
        max_stats = [hp(level, base_stats[0], evs[0], max(ranges[0]))]

        for counter, range in enumerate(ranges, 1):
            min_stats.append(other_stat(level, base_stats[counter], evs[counter], min(range), boosted=(nature_list[counter] == 1.1), reduced=(nature_list[counter] == 0.9)))
            max_stats.append(other_stat(level, base_stats[counter], evs[counter], max(range), boosted=(nature_list[counter] == 1.1), reduced=(nature_list[counter] == 0.9)))

        # Try again at the next level if the min stats and max stats are the same.
        if min_stats == max_stats:
            pass

        # Get the new stats, since there is some difference between the min and max.
        new_stats = input("Enter the stats at level " + str(level) + ", comma separated. ")
        new_stats = "".join(new_stats.split())
        new_stats = new_stats.split(",")
        new_stats = [int(c) for c in new_stats]

        old_ranges = ranges

        # Calculate the new IV ranges.
        calced_ranges = calc_iv_range(level, base_stats, new_stats, evs, nature)

        # Intersect the old ranges with the new ranges, such that
        # the maximum of the minimum of the 2 ranges becomes the minimum of the new range,
        # and the minimum of the maximum of the 2 ranges becomes the maximum of the new range.
        # For example, if we previously found the HP IV to be 26-29, and this time we found
        # 27-31, the new range would be 27-29.
        for counter, range in enumerate(calced_ranges):
            ranges[counter] = [max(old_ranges[counter][0], calced_ranges[counter][0]),
                               min(old_ranges[counter][1], calced_ranges[counter][1])]

        # print("New IV Ranges:", ", ".join([display_range(c) for c in ranges]), "\n")

    return ranges


def display_range(range):
    """ Return a representation of a range as the minimum and maximum separated by a dash. """
    return str(range[0]) + "-" + str(range[1])


# Driver method.
if __name__ == "__main__":
    # Level 48 Sassy Aggron with 252 HP, 160 Atk, and 96 Speed EVs.
    level = 48
    base_stats = [70, 110, 180, 60, 60, 50]
    evs = [252, 160, 0, 0, 0, 96]
    stats = [170, 137, 192, 77, 72, 71]
    nature = Nature.Sassy

    get_ivs(level, base_stats, stats, evs, nature)