#!/usr/bin/env python
# coding: utf-8

# The headers we need are as follows:
# 
# “Subject Subject_ID=” (ULAN ID) 
# 
# DONE: “Preferred_Term: Term_Text” (Primary Name)
# 
# DONE: “Non-Preferred_Term: Term_Text” (Display Name- with Display Name Flag)
# 
# “Non-Preferred_Term: Term_Text” (Secondary Names- there may be multiple)
# 
# “Record_Type” (Person or Corporate Body)
# 
# “Nationalities: Preferred_Nationality: Nationality_Code” (ULAN Nationality Code)
# 
# “Biographies: Preferred_Biography: Birth_Date” (Birth Date)
# 
# “Biographies: Preferred_Biography: Death_Date” (Death Date)
# 
# “Associative_Relationship: Relationship_Type: spouse of: VP_Subject_ID” (ulan_spouse_of_id)
# 
# “Associative_Relationship: Relationship_Type: sibling of: VP_Subject_ID (ulan_sibling_of_id)
# 
# “Associative_Relationship: Relationship_Type: child of: VP_Subject_ID” (ulan_child_of_id)
# 
# “Associative_Relationship: Relationship_Type: domestic partner of: VP_Subject_ID (ulan_domestic_partner_of_id)
# 
# “Associative_Relationship: Relationship_Type: grandchild of: VP_Subject_ID (ulan_grandchild_of_id)
# 
# “Associative_Relationship: Relationship_Type: donor of: VP_Subject_ID (ulan_donor_of_id)
# 

# In[ ]:





# In[430]:


# Libraries
import pandas as pd
import numpy as np
import sklearn as sk
import seaborn as sns
import matplotlib.pyplot as plt
import re
import datefinder
import substring as sub
from string import punctuation
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Data
with open("/Users/katrinamiller/Desktop/culturetech/ulan_scrape_xml/scrape_data_for_parse_build", "r", encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "xml")
    
# Data
with open("/Users/katrinamiller/Desktop/culturetech/ulan_scrape_xml/scrape_data_for_parse_build_ex", "r", encoding="utf8") as f2:
    contents2 = f2.read()
    soup2 = BeautifulSoup(contents2, "xml")
    
# Data
with open("/Users/katrinamiller/Desktop/culturetech/ulan_scrape_xml/scrape_data_for_parse_build_ex2", "r", encoding="utf8") as f3:
    contents3 = f3.read()
    soup3 = BeautifulSoup(contents3, "xml")
    
# How to Read:

# The structure of this program relies on hierarchy of purpose. 
# No dashes ("-") in front of the word indicates the overarching purpose of the section.
# One dash ("-") in front of the word indicates a subsection of the overarching purpose.
# Two dashes ("--") in front of the word indicates a sub-sub-section of the arching purpose, and so on. 
# The procedural paradigm is as follows: 
#     1: Intake 
#     2: Clean & Add Features (as programmatically convenient)
#     3: Export


#Data Lists for Future Dataframe Creation
ulan_id = []
primary_name = []
display_name = []
secondary_name = []
secondary_name2 = []
secondary_name3 = []
secondary_name4 = []
secondary_name5 = []
secondary_name6 = []
secondary_name7 = []
secondary_name8 = []
secondary_name9 = []
secondary_name10 = []
secondary_name11 = []
secondary_name12 = []
secondary_name13 = []
secondary_name14 = []
secondary_name15 = []
secondary_name16 = []
secondary_name17 = []
secondary_name18 = []
secondary_name19 = []
secondary_name20 = []
secondary_name21 = []
secondary_name22 = []
secondary_name23 = []
secondary_name24 = []
secondary_name25 = []
secondary_names_list = [secondary_name2, 
                        secondary_name3, 
                        secondary_name4, 
                        secondary_name5, 
                        secondary_name6, 
                        secondary_name7, 
                        secondary_name8, 
                        secondary_name9, 
                        secondary_name10, 
                        secondary_name11, 
                        secondary_name12, 
                        secondary_name13, 
                        secondary_name14, 
                        secondary_name15, 
                        secondary_name16, 
                        secondary_name17, 
                        secondary_name18, 
                        secondary_name19, 
                        secondary_name20, 
                        secondary_name21, 
                        secondary_name22, 
                        secondary_name23,
                        secondary_name24,
                        secondary_name25]
record_type = []
ulan_nationality_code = []
birthhdate = []
death_date = []
spouse_of = []
sibling_of = []
child_of = []
domestic_partner_of = []
grandchild_of = []
donor_of = []


# In[237]:


str = ((list(list(soup.find_all("Terms")[0])[1])[1]).text)
if "," in str: primary_name = ((str.split(","))[::-1])
else: primary_name = str
print(primary_name)
    


# In[110]:


# str(soup.find_all("Display_Name")[1]).split("<Display_Name>")[1].split("</Display_Name>")[0]
(str(list(soup.find_all("Non-Preferred_Term")[0])[3])).split("<Display_Name>")[1].split("</Display_Name>")[0]


# In[134]:


structure = soup.find_all("Display_Name")
structure
# list(structure)[]


# In[240]:


str2 = ((list(list(soup.find_all("Terms")[0])[1])[1]).text)
str2


# In[254]:


list(soup.find_all("Non-Preferred_Term"))


# In[251]:


if len(soup.find_all("Non-Preferred_Term")) == 1:
    pass
elif len(soup.find_all("Non-Preferred_Term")) > 1:
    secondary_names = 


# In[418]:


#3 Display_Name, non-preferred
list(soup.find_all("Non-Preferred_Term")[0])[3].text


# In[302]:


(soup.find_all("Nationality_Code")[0]).text[0:6]


# In[317]:


person_or_corporate_body = soup.find_all("Record_Type")[0].text


# In[ ]:


secondary_names = 0


# In[450]:


secondary_name_str = (list(soup.find_all("Non-Preferred_Term")[0]))[3].text
(list(soup.find_all("Non-Preferred_Term")[0]))


# In[ ]:


# Hi Robyn! 

# The following are the essential functions that need to be performed in a parse of the XML data from ULAN.
# These functions are commented in the code with section headers, as are how it corresponds to the document that
# Nicholas and Rachel drew up to ennumerate what they needed. Please see this document at the following URL:
# https://docs.google.com/document/d/1kebAWrewgsCoTtXNg-J34-tDsg-lDu09C3qU9ss8AIE/edit?usp=sharing
#
# I have left off the development of this parse function at a point where most of the constituent parts been tested 
# and checked, but they may not line up exactly. The function takes one parametter, a filepath (I strongly 
# recommend using an absolute filepath) and all parsing is performed from there on the file linked, which I predicate 
# on the data being XML, and not CSV or HTML. 
#
# You will notice that number 3 (“Non-Preferred_Term: Term_Text” (Display Name- with Display Name Flag))
# has been commented out. The initial solution I had for this part of the parse proved not to work at the 11th hour,
# and I haven't had time yet to continue working on the issue. Nicholas tells me you've solved this problem before,
# so hopefully it goes faster for you. I will update Nicholas on this as well so he knows the scope of your challenge.
# What I've got so far is a max count for secondary names columns & an iterator to add these columns at the end of
# function. 
#
# Please do not be afraid to reach out with any questions via Slack, email or text. 
# Thank you! 
# -Kat

def ulan_data_parser(filepath):
    
    # Data
    with open("filepath", "r", encoding="utf8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "xml")
    
    #Data Lists for Future Dataframe Creation. All of these lists will be updated a single value per pass.
    ulan_id = []
    primary_name = []
    display_name = []
    secondary_name = []
    record_type = []
    ulan_nationality_code = []
    birthhdate = []
    death_date = []
    spouse_of = []
    sibling_of = []
    child_of = []
    domestic_partner_of = []
    grandchild_of = []
    donor_of = []
    
    entries = list(soup.find_all("Parent_Subject_ID"))
    
    for entry in entries:
    
        # 1
        # “Subject Subject_ID=” (ULAN ID)
        ulan_id_str = (entry)[0]).text
        ulan_id.append(ulan_id_str)
        # print(ulan_id) #uncomment to print value

        # 2 
        # “Preferred_Term: Term_Text” (Primary Name)
        primary_name_str = ((list(list(entry.find_all("Terms")[0])[1])[1]).text)
        if "," in primary_name_str: 
            primary_name_data = ((str.split(","))[::-1])
        else: 
            primary_name_data = _str
        primary_name.append(primary_name_data)
        # print(primary_name_data) #uncomment to print value

#       # 3: INCOMPLETE
#       # “Non-Preferred_Term: Term_Text” (Display Name- with Display Name Flag)
#       # Amount of Non-Preferred Names for Determining Data Shape
        max_name_col_count = 0
        count_of_secondary_names_per_entry = len((entry.find_all("Non-Preferred_Term")[0]).find_all("Term_Text"))
        if max_name_col_count < count_of_secondary_names_per_entry:
            max_name_col_count = count_of_secondary_names_per_entry
        elif max_name_col_count = count_of_secondary_names_per_entry:
            pass
        else:
            pass
#         Index into Names
#         if (len(list(entry.find_all("Non-Preferred_Term")[0]))[3].text) > 0: 
#             nonpreferred_name_str = (list(entry.find_all("Non-Preferred_Term")[0])[1]).text
#             if "," in nonpreferred_name_str:
#                 nonpreferred_name = ((nonpreferred_name_str.split(","))[::-1])
#             else: nonpreferred_name = nonpreferred_name_str  
#         else: nonpreferred_name = none
#         # print(nonpreferred_name) #uncomment to print value

        # 4
        # “Non-Preferred_Term: Term_Text” (Secondary Names- there may be multiple)
        secondary_name_str = (list(entry.find_all("Non-Preferred_Term")[0]))[3].text
        secondary_name.append(secondary_name_str)
        # print(secondary_name_str) #uncomment to print value

        # 5
        # “Record_Type” (Person or Corporate Body)
        record_type_str = entry.find_all("Record_Type")[0].text
        record_type.append(record_type_str)
        # print(record_type_str) #uncomment to print

        # 6
        # “Nationalities: Preferred_Nationality: Nationality_Code” (ULAN Nationality Code)
        nationalities = (entry.find_all("Nationality_Code")[0]).text[0:6]
        ulan_nationality_code.append(nationalities)
        # print(nationalities) #uncomment to print

        #7
        # “Biographies: Preferred_Biography: Birth_Date” (Birth Date)
        if list(list(entry.find_all("Biographies")[0])[1])[5].text is True: 
            bio_birthdate = list(list(entry.find_all("Biographies")[0])[1])[5].text
        else: 
            bio_birthdate = "none"
        birthdate.append(bio_birthdate)
        # print(bio_birthdate) #uncomment to print

        # 8
        # “Biographies: Preferred_Biography: Death_Date” (Death Date)
        death_date_str = list(list(entry.find_all("Biographies")[0])[1])[7].text
        if len(death_date_str) > 0:
            birthhdate.append(death_date_str)
        else:
            birthhdate.append("none")
        # print(death_date_str) #uncomment to print


        # 9 - 14: Associative Relationships
        associative_relationship = (list(list(entry.find_all("Associative_Relationships")[0])[1])[1]).text

        if len(associative_relationship) >= 1:
            relatives_id = (list(list((list(entry.find_all("Associative_Relationships")[0])[1]))[3])[1]).text
        #     print(relatives_id)
            if associative_relationship == 'spouse of': 
                spouse_of.append("relatives_id")
                sibling_of.append("0")
                child_of.append("0")
                domestic_partner_of.append("0")
                grandchild_of.append("0")
                donor_of.append("0")
            elif associative_relationship == 'sibling of':
                spouse_of.append("0")
                sibling_of.append("relatives_id")
                child_of.append("0")
                domestic_partner_of.append("0")
                grandchild_of.append("0")
                donor_of.append("0")
            elif associative_relationship == 'child of':
                spouse_of.append("0")
                sibling_of.append("0")
                child_of.append("relatives_id")
                domestic_partner_of.append("0")
                grandchild_of.append("0")
                donor_of.append("0")
            elif associative_relationship == 'domestic partner of':
                spouse_of.append("0")
                sibling_of.append("0")
                child_of.append("0")
                domestic_partner_of.append("relatives_id")
                grandchild_of.append("0")
                donor_of.append("0")
            elif associative_relationship == 'grandchild of':
                spouse_of.append("0")
                sibling_of.append("0")
                child_of.append("0")
                domestic_partner_of.append("0")
                grandchild_of.append("relatives_id")
                donor_of.append("0")
            elif associative_relationship == 'donor of':
                spouse_of.append("0")
                sibling_of.append("0")
                child_of.append("0")
                domestic_partner_of.append("0")
                grandchild_of.append("0")
                donor_of.append("relatives_id")
            else: 
                print("Error in processing relationship data.")
                spouse_of.append("Error in processing relationship data.")
                sibling_of.append("Error in processing relationship data.")
                child_of.append("Error in processing relationship data.")
                domestic_partner_of.append("Error in processing relationship data.")
                grandchild_of.append("Error in processing relationship data.")
                donor_of.append("Error in processing relationship data.")
        else: 
        spouse_of.append("0")
        sibling_of.append("0")
        child_of.append("0")
        domestic_partner_of.append("0")
        grandchild_of.append("0")
        donor_of.append("0")

        
    #Build Dataframe Using Lists

    #Instantiate
    df = pd.Dataframe(columns= (ulan_id, 
                                primary_name, 
                                display_name, 
                                secondary_name,  
                                record_type, 
                                ulan_nationality_code, 
                                birthhdate, 
                                death_date, 
                                spouse_of, 
                                sibling_of, 
                                child_of, 
                                domestic_partner_of, 
                                grandchild_of, 
                                donor_of
                                   ))
    
    #3: INCOMPLETE
    # Add Secondary Names Columns
    for i in range[1:max_name_col_count]:
        column_name = ("secondary_name_" + i)
        df[column_name] = 
    
        
#   Save dataframe as CSV
    df.to_csv(r'\5-28-2020_ulan_scrape_parse.csv')


# In[ ]:



#     df["ulan_id"] = ulan_id
#     df["primary_name"] = primary_name
#     df["display_name"] = display_name
#     df["secondary_name"] = secondary_name
#     df["record_type"] = record_type
#     df["ulan_nationality_code"] = ulan_nationality_code
#     df["birthhdate"] = birthhdate
#     df["death_date"] = death_date
#     df["spouse_of"] = spouse_of
#     df["sibling_of"] = sibling_of
#     df["child_of"] = child_of
#     df["domestic_partner_of"] = domestic_partner_of
#     df["grandchild_of"] = grandchild_of
#     df["donor_of"] = donor_of


#         df = pd.DataFrame(columns= (ulan_id, 
#                                     primary_name, 
#                                     display_name, 
#                                     secondary_name, 
#                                     secondary_name2, 
#                                     secondary_name3, 
#                                     secondary_name4, 
#                                     secondary_name5, 
#                                     secondary_name6, 
#                                     secondary_name7, 
#                                     secondary_name8, 
#                                     secondary_name9, 
#                                     secondary_name10, 
#                                     secondary_name11, 
#                                     secondary_name12, 
#                                     secondary_name13, 
#                                     secondary_name14, 
#                                     secondary_name15, 
#                                     secondary_name16, 
#                                     secondary_name17, 
#                                     secondary_name18, 
#                                     secondary_name19, 
#                                     secondary_name20, 
#                                     secondary_name21, 
#                                     secondary_name22, 
#                                     secondary_name23, 
#                                     secondary_name24, 
#                                     secondary_name25, 
#                                     record_type, 
#                                     ulan_nationality_code, 
#                                     birthhdate, 
#                                     death_date, 
#                                     spouse_of, 
#                                     sibling_of, 
#                                     child_of, 
#                                     domestic_partner_of, 
#                                     grandchild_of, 
#                                     donor_of
#                                    )
#                          )


# In[427]:


# “Non-Preferred_Term: Term_Text” (Secondary Names- there may be multiple)
(list(soup.find_all("Non-Preferred_Term")[0]))[3].text


# In[442]:


# Amount of Non-Preferred Names for Determining Data Shape

max_name_col_count = 0
count_of_secondary_names_per_entry = len((soup.find_all("Non-Preferred_Term")[0]).find_all("Term_Text"))
if max_name_col_count < count_of_secondary_names_per_entry:
    max_name_col_count = count_of_secondary_names_per_entry
elif max_name_col_count = count_of_secondary_names_per_entry:
    pass
else:
    pass


# In[353]:


# 8
# “Biographies: Preferred_Biography: Death_Date” (Death Date)
death_date_str = list(list(soup.find_all("Biographies")[0])[1])[7].text
if len(death_date_str) > 0:
    birthhdate.append(death_date_str)
else:
    birthhdate.append("none")
# print(bio_deathdate) #uncomment to print


# In[412]:


associative_relationship = (list(list(soup3.find_all("Associative_Relationships")[0])[1])[1]).text

if len(associative_relationship) >= 1:
    relatives_id = (list(list((list(soup3.find_all("Associative_Relationships")[0])[1]))[3])[1]).text
    print(relatives_id)
    if associative_relationship == 'spouse of': 
        relationship = 'spouse of'
    elif associative_relationship == 'sibling of':
        relationship = 'sibling of'
        relatives_id = (list(list((list(soup3.find_all("Associative_Relationships")[0])[1]))[3])[1]).text
    elif associative_relationship == 'child of':
        relationship = 'child of'
    elif associative_relationship == 'domestic partner of':
        relationship = 'domestic partner of'
    elif associative_relationship == 'grandchild of':
        relationship = 'grandchild of'
    elif associative_relationship == 'donor of':
        relationship = 'donor of'
    else: 
        relationship = associative_relationship
else: 
    relationship = None
    relatives_id = None


# In[409]:


relatives_id = (list(list((list(soup3.find_all("Associative_Relationships")[0])[1]))[3])[1]).text
print(relatives_id)


# In[ ]:


# “Associative_Relationship: Relationship_Type: spouse of: VP_Subject_ID” (ulan_spouse_of_id)

# “Associative_Relationship: Relationship_Type: sibling of: VP_Subject_ID (ulan_sibling_of_id)

# “Associative_Relationship: Relationship_Type: child of: VP_Subject_ID” (ulan_child_of_id)

# “Associative_Relationship: Relationship_Type: domestic partner of: VP_Subject_ID (ulan_domestic_partner_of_id)

# “Associative_Relationship: Relationship_Type: grandchild of: VP_Subject_ID (ulan_grandchild_of_id)

# “Associative_Relationship: Relationship_Type: donor of: VP_Subject_ID (ulan_donor_of_id)


# In[67]:


# “Non-Preferred_Term: Term_Text” (Display Name- with Display Name Flag)
str(soup.find_all("


# In[86]:


# Name

(str(soup.find_all("Display_Name")[0])).split("<Display_Name>")[1].split("</Display_Name>")[0]


# In[48]:


# Nationality

str(soup.find_all("Nationality_Code")[0]).split("<Nationality_Code>")[1].split("</Nationality_Code>")[0].split("/")[0]


# In[27]:


tree = ET.parse("/Users/katrinamiller/Desktop/culturetech/data/ulan1.xml")
root = tree.getroot()

