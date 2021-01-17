from math import floor
from enum import Enum


stats_names = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]


class Nature(Enum):
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
        txt = self.name

        if self.value != [1] * 6:
            boosted_index = self.value.index(1.1)
            reduced_index = self.value.index(0.9)

            txt += " (+" + stats_names[boosted_index] + ",-" + stats_names[reduced_index] + ")"

        return txt


def hp(level, base, ev, iv):
    return floor(level / 100 * (2 * base + iv + floor(ev / 4))) + level + 10


def other_stat(level, base, ev, iv, boosted=False, reduced=False):
    assert not (boosted and reduced)

    stat = floor(level / 100 * (2 * base + iv + floor(ev / 4))) + 5

    if boosted:
        stat = floor(stat * 1.1)

    elif reduced:
        stat = floor(stat * 0.9)

    return stat


def calc_iv_range(level, base_stats, stats, evs, nature):
    ivs = [[0, 31]] * 6
    nature_list = nature.value

    for index, iv_range in enumerate(ivs):
        min, max, min_found, max_found = 0, 31, False, False

        for iv in range(iv_range[0], iv_range[1] + 1):
            if index != 0:
                this_stat = other_stat(level, base_stats[index], evs[index], iv, boosted=(nature_list[index] == 1.1), reduced=(nature_list[index] == 0.9))

                if this_stat == stats[index]:
                    if not min_found:
                        min_found = True
                        min = iv

                    if this_stat != other_stat(level, base_stats[index], evs[index], iv + 1, boosted=(nature_list[index] == 1.1), reduced=(nature_list[index] == 0.9)):
                        max_found = True
                        max = iv

            else:
                this_stat = hp(level, base_stats[index], evs[index], iv)

                if this_stat == stats[0]:
                    if not min_found:
                        min_found = True
                        min = iv

                    if this_stat != hp(level, base_stats[0], evs[0], iv + 1):
                        max_found = True
                        max = iv

            ivs[index] = [min, max]

    return ivs


def get_ivs(level, base_stats, stats, evs, nature):
    ranges = calc_iv_range(level, base_stats, stats, evs, nature)
    # print(", ".join([display_range(c) for c in ranges]))
    nature_list = nature.value

    while not all(max(c) == min(c) for c in ranges) and level <= 100:
        level += 1

        min_stats = []
        max_stats = []

        for counter, range in enumerate(ranges):
            if counter != 0:
                min_stats.append(other_stat(level, base_stats[counter], evs[counter], min(range), boosted=(nature_list[counter] == 1.1), reduced=(nature_list[counter] == 0.9)))
                max_stats.append(other_stat(level, base_stats[counter], evs[counter], max(range), boosted=(nature_list[counter] == 1.1), reduced=(nature_list[counter] == 0.9)))

            else:
                min_stats.append(hp(level, base_stats[counter], evs[counter], min(range)))
                max_stats.append(hp(level, base_stats[counter], evs[counter], max(range)))

        if min_stats != max_stats:
            new_stats = input("Enter the stats at level " + str(level) + ", comma separated. ")
            new_stats = "".join(new_stats.split())
            new_stats = new_stats.split(",")
            new_stats = [int(c) for c in new_stats]

            old_ranges = ranges
            calced_ranges = calc_iv_range(level, base_stats, new_stats, evs, nature)

            for counter, range in enumerate(calced_ranges):
                ranges[counter] = [max(old_ranges[counter][0], calced_ranges[counter][0]), min(old_ranges[counter][1], calced_ranges[counter][1])]

            # print("New IV Ranges:", ", ".join([display_range(c) for c in ranges]), "\n")

    return ranges


def display_range(range):
    return str(range[0]) + "-" + str(range[1])


if __name__ == "__main__":
    level = 48
    base_stats = [70, 110, 180, 60, 60, 50]
    evs = [252, 160, 0, 0, 0, 96]
    stats = [170, 137, 192, 77, 72, 71]
    nature = Nature.Sassy

    get_ivs(level, base_stats, stats, evs, nature)
