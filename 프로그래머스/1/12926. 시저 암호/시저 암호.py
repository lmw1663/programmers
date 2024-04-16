def solution(s, n):
    encrypted_text = ''
    for char in s:
        # 알파벳인 경우
        if char.isalpha():
            # 대문자인 경우
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            # 소문자인 경우
            elif char.islower():
                encrypted_text += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        # 공백인 경우
        else:
            encrypted_text += char
    return encrypted_text