import pandas as pd
import re
# Create a dict
dict_data = {}

# Open the suppliernames.txt file
with open('suppliernames.txt','r') as df:
    # Read each line
    for line in df:       
        # Split each line by ","
        for kv in [line.split(",")]:
            # Put id and the value inside the dict
            dict_data.setdefault(kv[0],[]).append(kv[1].rstrip("\n"))

#print(dict_data)
#dict_data.columns=['Id','SupplierName']
            
# Transfer the dict to dataframe
df2 = pd.DataFrame.from_dict(dict_data,orient='index',columns=['SupplierName'])
#print(df2)

######################################
## Open the invoice.txt file
result_list=[]
with open('invoice.txt') as f:
    findtxt = "'word':"
    findtxt_2 = "line_id'"
    for line in f:
        pos1=line.find(findtxt)
        pos2=line.find(findtxt_2)
        temp = line[pos1:pos2]
        result_list.append(eval(temp[7:-3]))
        #print(temp[7:-2])
#print(result_list)


######################################
## Make an interection between the suppliername and the invoice supplier name

##for index, row in df2.iterrows():

#for line in result_list:
#    #k = eval(line)
#    flag = 0
#    for index, row in df2.iterrows():
#        m = df2['SupplierName'].values[flag]
#        flag = flag + 1
#        if line == m:
#            print(line)
           
result_list_3 = df2['SupplierName'].values.tolist()
result = list(set(result_list) & set(result_list_3))
##result = set(result_list).intersection(result_list_3)
print(result)

#print(pd.merge(df2['SupplierName'],result_list))
