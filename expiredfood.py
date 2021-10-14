#item = {} #list of items 
new_item = input('Name and exp date: enter in form "Name Exp"') #Item and Expiration Date
    #Split Name and Product into 2 data points
split_input = [new_item.split(':')] #seperate product and expiration date 
item = dict(new_item.split(":") for i in new_item);
"""for key, value in item():
    print(key, ' : ', value)

    """
