def countRocks(dist, rocks):
    start = 0
    count = 0
    for r in rocks:
        if r-start < dist:
            count += 1
        else:
            start = r
    return count

def solution(distance, rocks, n):
    maxDist = 0
    rocks.sort()
    start = 0
    end = distance
    rocks.append(distance)
    
    while start <= end:
        flagDist = (start+end)//2
        if countRocks(flagDist, rocks) <= n:
            maxDist = flagDist
            start = flagDist + 1
        else:
            end = flagDist - 1
        
    
    return maxDist