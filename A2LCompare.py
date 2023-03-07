
# Script to extract signals from 2 different A2L Files and prepare a list of newly added, removed and unchanged variables.
# Author : Shiva

import re

class DiffCreator():
    def __init__(self,file1,file2,file_type):
        self.file1 = file1
        self.file2 = file2
        self.file_type = file_type
        if self.file_type == 'a2l':
            self.common_var = self.A2LCompare()[0]
            self.new_var= self.A2LCompare()[1]
            self.old_var = self.A2LCompare()[2]
        elif self.file_type =='can':
            self.common_var = self.CANCompare()[0]
            self.new_var= self.CANCompare()[1]
            self.old_var = self.CANCompare()[2]
        else:
            print('Please select file_type')

    def CANReader(self,file_path):
        emp_list1 = []
        emp_list2 = []
        with open(file_path) as f:
            if file_path.endswith(".dbc"):
                [emp_list1.append((line.split(':')[1])) \
             for line in f.readlines() if 'SG_' in line]
        for val in emp_list1:
            var = val.split('\n')
            emp_list2.append(var[0])
        return emp_list2

    def A2LReader(self,file_path):
        '''
        Read A2L File and fetch the signals of pattern
        '''
        emp_list1 = []
        emp_list2 = []
        with open(file_path) as f:
            [emp_list1.append((line.split('/begin MEASUREMENT ')[1])) \
             for line in f.readlines() if 'begin MEASUREMENT' in line]
        for val in emp_list1:
            var = val.split('\n')
            emp_list2.append(var[0])
        return emp_list2
            

    def A2LCompare(self):
        '''
        Read both the A2L Files , create a list of common variables, newly added variables and removed variables.
        '''
        file1_list = self.A2LReader(self.file1)
        file2_list = self.A2LReader(self.file2)
        common_var = []
        new_var = []
        old_var = []
        for var1 in file1_list:
            if var1 in file2_list:
                common_var.append(var1)

        for var2 in file1_list:
            if var2 not in file2_list:
                new_var.append(var2)

        for var3 in file2_list:
            if var3 not in file1_list:
                old_var.append(var3)

        fin = [common_var, new_var , old_var]
        return fin

    
    def CANCompare(self):
        '''
        Read both the A2L Files , create a list of common variables, newly added variables and removed variables.
        '''
        file1_list = self.CANReader(self.file1)
        file2_list = self.CANReader(self.file2)
        common_var = []
        new_var = []
        old_var = []
        for var1 in file1_list:
            if var1 in file2_list:
                common_var.append(var1)

        for var2 in file1_list:
            if var2 not in file2_list:
                new_var.append(var2)

        for var3 in file2_list:
            if var3 not in file1_list:
                old_var.append(var3)

        fin = [common_var, new_var , old_var]
        return fin

    def CommonVar(self):
        '''
        Fetch and set common variables to a list.
        '''
        return self.common_var

    def NewVar(self):
        '''
        Fetch and set new variables to a list.
        '''
        return self.new_var

    def OldVar(self):
        '''
        Fetch and set old variables to a list.
        '''
        return self.old_var
                
        
	
        
        

    
            
        
