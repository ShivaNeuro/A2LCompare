
from A2LCompare import DiffCreator

file1 = r'C:\Users\shivaram.boddepalli_\Desktop\Files\New\scu_primary_generic.a2l'
file2 = r'C:\Users\shivaram.boddepalli_\Desktop\Files\Old\scu_primary_generic.a2l'

Diff = DiffCreator(file1,file2,'a2l')
print("Common ")
print(Diff.CommonVar())
print("**************")
fil = open('Report.html','w')
fil.write("CommonVariables" + "<br />")
for i in Diff.CommonVar():
    message = i
    fil.write(message+ "<br />")
fil.close()
    
    
print("New\n")
print(Diff.NewVar())
print("**************")
print("Old\n")
print(Diff.OldVar())









    
