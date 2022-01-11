def max_sum_subarray(arr):
    size=len(arr)
    curr_sum=0
    max_so_far=arr[0]
    st=0
    end=0
    poi=0
    for i in range(0,size):
        curr_sum=curr_sum+arr[i]
        if(max_so_far<curr_sum):
            max_so_far=curr_sum
            st=poi
            en=i
        if(curr_sum<0):
            curr_sum=0
            poi=i+1
    print('max sum subarray',max_so_far)
    print('start index',st)
    print('end index',en)

arr=[2,3,4,6,-4,-5,8,7,3,4,-2]
max_sum_subarray(arr)