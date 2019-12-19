import re

if __name__ == "__main__":
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
    r1 = "in"
    x1 = re.findall(r1, txt)  # output: ["in", "in", "in"]
    x2 = re.split(r1, txt)  # output: ["The ra", " ", " Spa"]
    x3 = re.split("\s", txt, 1)  # output: ["The", "rain in Spain"] -> only split once
    x4 = re.sub("\s", "9", txt)  # output: The9rain9in9Spain
    x5 = re.sub("\s", "9", txt, 2)  # output: The9rain9in Spain
    print(x)
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    '''
    .span() returns a tuple containing the start-, and end pos of the match
    .string returns the string passed into the function
    .group() returns the part of the string where there was a match
    '''
    print("===================")
    a = re.search("a.", txt).group()
    print(a)  # <re.Match object; span=(5,7), match='ai'>
    #    print (a.span())  # (5,7)
    #    print (a.string)  # The rain in Spain
    #    print (a.group())
    print("---------------------")

    lun_q = 'Lun:\s*(\d+(?:\s+\d+)*)'
    s = '''Lun: 0 1 2 3 295 296 297 298'''
    r = re.search(lun_q, s)
    if r:
        luns = r.group(1).split()
        print(luns)  # output: ['0', '1', '2', '3', '295', '296', '297', '298']
