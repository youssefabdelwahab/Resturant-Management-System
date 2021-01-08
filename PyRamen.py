#!/usr/bin/env python
# coding: utf-8

# In[120]:


import csv 


# In[121]:


import json


# In[ ]:


for i in range()


# In[123]:


menu = {}
with open('menu_data.csv' , "r" ) as csv_file: 
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader: 
        a=1
        menu[row[0]] = {
            "category": row[1],
            "description": row[2],
            "price": float(row[3]),
            "cost": float(row[4]),
        }
#         menu.append(row)
# print(row)
# print(menu["black sesame creme brulee"])
print(json.dumps(menu, indent=4))


# In[124]:


sales = {}
with open('sales_data.csv' , 'r') as csv_file2: 
    csv_reader2 = csv.reader(csv_file2)
    header2 = next(csv_reader2)
    for line in csv_reader2:
        the_item = line[4]
        quantity = float(line[3])
        if the_item not in sales: 
            sales[the_item] =  {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
            }
            
        sales[the_item]["01-count"] += quantity
        revenue = menu[the_item]["price"] * quantity
        cost = menu[the_item]["cost"] * quantity
        sales[the_item]["02-revenue"] = sales[the_item]["02-revenue"] + revenue
        sales[the_item]["03-cogs"] = sales[the_item]["03-cogs"] + cost
        sales[the_item]["04-profit"] = sales[the_item]["04-profit"] + (revenue - cost)


# In[125]:


sales


# In[ ]:



        
        
        
        
        
        
        
        
        
        


# In[ ]:





# In[ ]:




