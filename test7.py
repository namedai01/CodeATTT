f = open("inp.txt", encoding="utf8")
str = f.read()

length = len(str)

s2 = '.,/:\n? \\-_{}[]()\'\"~`?!@#$%^&*+=|;<>'
s1 = 'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = 'AAÂAEEÊIIOOÔOUUYAAÂAEEÊIIOOÔOUUYĂĂĐĐIIUUƠƠƯƯAAAAÂÂÂÂÂÂÂÂÂÂĂĂĂĂĂĂĂĂĂĂEEEEEEÊÊÊÊÊÊÊÊÊÊIIIIOOOOÔÔÔÔÔÔÔÔÔÔƠƠƠƠƠƠƠƠƠƠUUUUƯƯƯƯƯƯƯƯƯƯYYYYYYYY'


# initDict = dict(zip(s1, s0))

firstC = ""
secondC = ""
thirdC = ""
def frequency(str, firstC, secondC, thirdC):
    res = {}
    for i in range(0, length):
        c = str[i]
        if (c not in s2):
            # Monogram
            firstC = s0[s1.index(c)] if (c in s1) else c.upper()
            res[firstC] = res.get(firstC, 0) + 1

            # Biagram
            if (i != 0 and secondC != ""):
                bia = secondC + firstC
                res[bia] = res.get(bia, 0) + 1
                
                #trigram
                if (i != 1 and thirdC != ""):
                    tria = thirdC + bia
                    res[tria] = res.get(tria, 0) + 1
            
            thirdC = secondC
            secondC = firstC
    return res

print(frequency(str, firstC, secondC, thirdC))




