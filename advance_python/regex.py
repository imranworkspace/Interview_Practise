import re
passage = "This approach counts the occurrences of each 'imrans' in the list and stores the counts in a dictionary, where the keys are the distinct imrans in the list, and the imrans are the counts of each imrans. You can then access the counts for each imran as needed.imran"
pattern='imran'

match = re.findall(pattern,passage)
print(match)
print(len(match))

# search imran
text='my name is imran'
match_name = 'imran'
re_object = re.compile(match_name)
search_done = re.search(re_object,text)
print('search_done ',search_done)