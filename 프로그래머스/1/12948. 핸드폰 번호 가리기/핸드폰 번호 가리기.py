def solution(phone_number):
    lengthtokeep = len(phone_number)-4
    replaced_string = '*'*lengthtokeep + phone_number[lengthtokeep:]
        
    return replaced_string