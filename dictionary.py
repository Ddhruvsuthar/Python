n=int(input("enter limit:"))
dict1 = {}
for i in range(n):
    name=str(input("enter  name "))
    mob=eval(input("enter number "))
    dict2 = ({name:mob})
    dict1.update(dict2)

a=str(input("type L for veiw full dictionary or type S for a Particular Search 2"))
L=""
S=""
if L==a:
   print(dict1)
elif S==a:
    n=str(input("please enter the name of the person for contact no."))
    print("the person contact no is", dict1[n])
else:
    print("incorect")








