def solution(s):
    word_to_number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    answer = ''
    word = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            word += char
            if word in word_to_number:
                answer += word_to_number[word]
                word = ''
    return int(answer)