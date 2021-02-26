def recite(start_verse, end_verse):
    # start through end
    start_to_end = range(start_verse, end_verse + 1, 1)
    result = []
    if start_verse == end_verse:
        result.append(calculateLine(start_verse))
    else:
        for count in start_to_end:
            result.append(calculateLine(count))
    return result


def calculateLine(count):
    v2_map = mapVerseTwo()
    final_line = partOne(count)
    if count == 1:
        final_line += verseTwoOneLine()
    else:
        span = range(count, 0, -1)
        for line in span:
            final_line += v2_map.get(line)
    return final_line


def partOne(start_verse):
    day = numToString(start_verse)
    p1 = "On the " + day + " day of Christmas my true love gave to me: "
    return p1


def numToString(num):
    switcher = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    return switcher.get(num, "Invalid")


def verseTwoOneLine():
    return "a Partridge in a Pear Tree."


def mapVerseTwo():
    switcher = {
        1: "and a Partridge in a Pear Tree.",
        2: "two Turtle Doves, ",
        3: "three French Hens, ",
        4: "four Calling Birds, ",
        5: "five Gold Rings, ",
        6: "six Geese-a-Laying, ",
        7: "seven Swans-a-Swimming, ",
        8: "eight Maids-a-Milking, ",
        9: "nine Ladies Dancing, ",
        10: "ten Lords-a-Leaping, ",
        11: "eleven Pipers Piping, ",
        12: "twelve Drummers Drumming, "
    }
    return switcher
