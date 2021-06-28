def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p1 == p2[0:len(p1)]:
            return False
    return True