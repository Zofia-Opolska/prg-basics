def f(dates):
    import re
    pattern = r"\d{2}/\d{2}/\d{4}"  #dlaczego jak nie dam r to printuje tez pattern ?????
    # pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(pattern,dates)

dates = "2021-1-3;05/12/2024:1998-12-11,9 maj 2007;;31/03/2021,,1/9/2011"
print(f(dates))