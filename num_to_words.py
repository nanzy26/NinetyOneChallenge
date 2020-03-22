import argparse

nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million',
        1000000000: 'billion', 1000000000000: 'trillion'}

kilo = 1000


def check_word(word, ignore=None):
    """
    checking for valid numbers. Ignore check
    """
    ignore = ignore or []
    # remove ignored chars
    _word = word.lstrip('-')
    for c in ignore:
        _word.replace(c, '')
    if _word.isnumeric():
        return True
    if any([c.isdigit() for c in _word]):
        raise ValueError('Not a valid number')
    return False


def sentence_to_num(sentence):
    """
    converts text to int after checking for validity
    :param sentence: text from input file
    :return: int value of the number
    """
    words = sentence.split(' ')
    output = []
    for word in words:
        if check_word(word, ignore=None):
            output.append(word)

    return [int(i) for i in output]


def num_below_thousand(num):
    """
    handles numbers below a thousand and refers to nums dictionary
    :param num: int value of number
    :return: word representation of number below 1000
    """
    assert (num >= 0)
    if num == 0:
        return ''
    if num < 20:  # anything under 20 has its own number
        return nums[num]
    elif num < 100:
        if num % 10 == 0:
            return (nums[num // 10 * 10]).strip()
        else:
            return (nums[num // 10 * 10] + '-' + nums[num % 10]).strip()
    elif num < kilo:
        end = num_below_thousand(num % 100)
        join = ''
        if end:
            join = ' and ' if num % 100 < 100 else ' '
        return (nums[num // 100] + ' hundred' + join + end).strip()


def convert_number(num, scale=1):
    """
    converts number to words
    :param num: int value of number
    :param scale: power of 1000
    :return: word representation of number
    """
    if num < 1000:
        p = nums[scale] if scale > 1 else ''
        return (num_below_thousand(num) + ' ' + p + '').strip()
    else:
        scale *= 1000
        top, bot = divmod(num, 1000)
        result = convert_number(top, scale)
        last = convert_number(bot, scale // 1000) if bot else ''
        join = ''
        if bot:
            if bot < 100:
                join = ' and '
            else:
                join = ', '
        return (result + join + last).strip()


def num_2_word(num):
    """
    handles special cases like 0 and negative numbers
    :param num: int value of number
    :return: word representation of number
    """
    if num == 0:
        return 'zero'
    if num < 0:
        return 'minus ' + convert_number(abs(num))
    else:
        return convert_number(num)


def main():
    parser = argparse.ArgumentParser(description='Put txt file path here')
    parser.add_argument('-f', '--file', help='Enter file path here')
    args = parser.parse_args()

    if args.file:
        with open(args.file) as file:
            txt = file.readline()
    try:
        num = sentence_to_num(txt)
        words = [num_2_word(n) for n in num]
        [print(w) for w in words]
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
