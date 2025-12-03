def month(n):
        arr=[
        'Styczeń',
        'Luty',
        'Marzec',
        'Kwiecień',
        'Maj',
        'Czerwiec',
        'Lipiec',
        'Sierpień',
        'Wrzesień',
        'Październik',
        'Listopad',
        'Grudzień'
    ]
        for a in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if n==a:
                return arr[a-1]
        
print(month(1))
print(month(12))
print(month(17))
print(month(2))
print(month(5))
print(month(7))
print(month(8))

