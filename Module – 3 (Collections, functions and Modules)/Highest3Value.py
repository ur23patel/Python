my_dict = {"A":3,"B":4,"H":1,"K":8,"T":0}

my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
