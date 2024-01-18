# months = {'imran'}
months = set(["January","February", "March", "April", "May", "June"])    
# discard() not raised any error if item is avaialble or not
# months.discard("January");    
# months.discard("Imran");    

# remove() not raised an error if item is avaialble or not 
# raised an error KeyError: 'January'
# months.remove("January");    
# months.remove("Imran");    

months.clear()

print(months)
print(type(months))