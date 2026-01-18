def f(dates):
    import re
    pattern = r'\d{4}-\d{2}-\d{2}'
    result = re.findall(pattern,dates)
    return result

dates = "2021-12-03;05/12/2024:1998-12-11,9 maj 2007;;31/03/2021,,1/9/2011"
print(f(dates))