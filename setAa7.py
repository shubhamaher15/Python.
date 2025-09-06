my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 1}

sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)

sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)
