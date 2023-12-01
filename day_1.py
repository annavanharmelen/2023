# Define a function that returns the sum of all calibration values given a list of calibration strings  
def get_calibration_sum(calibration_strings):
        
    # get all numbers from each line
    all_calibration_values = []
    for code in calibration_strings:
        all_calibration_values.append([x for x in code if x.isdigit()])

    # grab calibration values
    calibration_values = []
    for code in all_calibration_values:
        if len(code) > 1:
            calibration_values.append(int("".join([code[0], code[-1]])))
        else:
            calibration_values.append(int("".join([code[0], code[0]])))

    # combine into sum of all calibration values
    return sum(calibration_values)

## Part 1
# open the file
calibration_txt = open("input_day1.txt", "r")

# read each line into list
calibration_string = calibration_txt.read()
calibration_strings = calibration_string.strip().split("\n")

# get calibration sum
print('Answer to part 1: ' + str(get_calibration_sum(calibration_strings)))

## Part 2
# define what to look for
word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# look, I also really hate this solution, but it works, so sue me
replace_words = ["on1e", "tw2o", "thr3ee", "fo4ur", "fi5ve", "si6x", "se7ven", "ei8ght", "ni9ne"]

# find all starting indexes of word-digits and replace them with the replace-words
new_calibration_strings = []

for code in calibration_strings:
    digit_idxs = []
    digits = []
    for digit in word_digits:
        if code.find(digit) > -1:
            digit_idxs.append(code.find(digit))
            digits.append(digit)

    for idx in sorted(digit_idxs):
        code = code.replace(
            digits[digit_idxs.index(idx)],
            replace_words[word_digits.index(digits[digit_idxs.index(idx)])],
        )
    
    new_calibration_strings.append(code)

# get calibration sum
print('Answer to part 2: ' + str(get_calibration_sum(new_calibration_strings)))
