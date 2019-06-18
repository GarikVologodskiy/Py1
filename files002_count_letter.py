with open (r"C:\Distrib\Python\dataset_3363_2.txt", "r") as file_in:
    r = file_in.read().strip().lower()
    count = 0
    c = 0
    for i in r:
        if r.count(i) > count:
            count = r.count(i)
            c = i
    with open (r"C:\Distrib\Python\dataset_3363_3.txt", "w") as file_out:
        file_out.write(str(c))
        file_out.write(" ")
        file_out.write(str(count))
           
