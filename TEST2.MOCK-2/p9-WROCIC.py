def f(value: int) -> int:
    count = 0
    
    with open("data.csv", "r") as file:
        for line in file:
            line = line.split(",")
            
            if (str(line[9]) != "salary"):
                if (int(line[9]) >= value):
                    count += 1
                    
    return count