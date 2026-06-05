listik = ["reoig" , "giperip"]
def whoLikesThis(lst):
    count = len(lst)
    if lst == []:
        mes =  'no one likes this'
    elif count == 1:
        mes =  (lst[0] + " likes this")
    elif count == 2:
        mes =  (lst[0] + " and " + lst[1] + " like this")
    elif count == 3:
        mes =  (lst[0] + " , " +  lst[1] + " and "+  lst[2] + " like this ")
    else:
        mes =  (lst[0] + " , "+  lst[1] + " and " +  count-2 + " others like this")
    return mes


massege = whoLikesThis(listik)
print(massege)

