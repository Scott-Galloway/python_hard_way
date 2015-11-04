tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip \n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


r_test = "This is a test for r formatting \' \""

print "R %r" % r_test
print "S %s" % r_test

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
