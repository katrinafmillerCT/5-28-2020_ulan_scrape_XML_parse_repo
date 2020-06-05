# 5-28-2020_ulan_scrape_XML_parse_repo
Python file containing the essential functions of a parse of the ULAN scrape dated 5/28/2020. Intended for use with the original XML scrape file. 

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
