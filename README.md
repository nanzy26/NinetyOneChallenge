# NinetyOneChallenge
Coding challenge - convert numbers to words

To run the script with the test input cases, please do the following:

  python num_2_words.py -f tests/input_files/input_1.txt
  
The script first converts the sentence/text to an integer number, then proceeds to turn the number into words.
It does this by splitting up the numbers into whether the number is above thousand or below thousand as we have a dictionary of unique words that can be used to build words.

Anything below 100 can be looked up in the dictionary and anything below 1000 can be looked up recursively within the function after splitting the number again. 

The script handles negative numbers but not decimal points. There is a test file: test_num_to_words.py which has numerous cases.

