def solution(food):
    ads = ""
    for i in range(len(food)):
        if i!=0:
            if food[i]%2==0:
                ads = ads+ str(i)*(food[i]//2)
                print(str(i))
            else:
                ads = ads+ str(i)*((food[i]-1)//2)
                print(str(i))
    adk = ads[::-1]
    
    total = ads+"0"+adk
    
    return total