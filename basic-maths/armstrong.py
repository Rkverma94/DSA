'''
    To find the arm strong number ? true : false
    timecomplexity : O(n)
    space complexity : O(n)'
    
'''
def armstrong(num):
    numStr = str(num)
    genNum = 0
    for i in numStr:
        i = int(i)
        genNum = genNum + i**len(numStr)
    return genNum == num
print(armstrong(3236))
