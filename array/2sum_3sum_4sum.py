def two_sum(arr,target):
    hm={}

    for ind, no in enumerate(arr):
        if no in hm:
            return [hm[no],ind]
        hm[target-no]=ind
    return []
print(two_sum([2,7,11,15],9))

def three_sum(arr,target):
    arr.sort()
    res=[]
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l=i+1
        r=len(arr)-1
        while l<r:
            s=arr[i]+arr[l]+arr[r]
            if s==target:
                res.append([arr[i],arr[l],arr[r]])
                while l<r and arr[l]==arr[l+1]:
                    l+=1
                while l<r and arr[r]==arr[r-1]:
                    r-=1
                l+=1
                r-=1
            elif s<target:
                l+=1
            else:
                r-=1
    return res