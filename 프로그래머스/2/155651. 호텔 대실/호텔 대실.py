from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda x:x[0])
    for book in book_time:
        start = num(book[0])
        end = num(book[1])+10
        if rooms!=[] and rooms[0]<=start:
            heappop(rooms)
        heappush(rooms, end)
    return len(rooms)

def num(time):
    total = 0
    total = int(time[:2])*60 + int(time[3:])
    return total