with open (r"C:\Distrib\Python\dataset_3363_3.txt", "r") as file_in:
    r = file_in.read().strip().lower()
    s = [str(i) for i in r.split()]
    count = 0
    c = 0
    for i in s:
        if s.count(i) > count:
            count = s.count(i)
            c = i
    with open (r"C:\Distrib\Python\dataset_3363_4.txt", "w") as file_out:
        file_out.write(str(c) + " " + str(count))      
