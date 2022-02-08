def breakingRecords(scores):
    # Write your code here
    h_count=l_count=0
    highest_score=lowest_score=scores[0]
    for x in scores:
            
        if x > highest_score:
            highest_score=x
            h_count+=1
        elif x< lowest_score:
            lowest_score=x
            l_count+=1
    print(h_count,l_count)
# breakingRecords([12,24,10,24])
# breakingRecords([10,5,20,20,4,5,2,25,1])
breakingRecords([3, 4, 21 ,36, 10 ,28, 35,5 ,24,42])
