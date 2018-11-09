start_char="\002"
end_char="\003"

def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert start_char not in s and end_char not in s, "Input string cannot contain STX and ETX characters"
    s = start_char + s + end_char  # Add start and end of text marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string


def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith(end_char)][0]  # Find the correct row (ending in ETX)
    return s.rstrip(end_char).strip(start_char)  # Get rid of start and end markers