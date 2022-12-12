pat = 'Name=%s Number=%d What=%s'

x1 = 'sdfsdfd'
x2 = 15
x3 = 'p14'

l = pat % (x1, x2, x3)
print(l)
#
# pi = 3.142435354
# l = "pi = {0:.3f} + {1:s[3,]}".format(pi, '28543')





pat = 'Name={!s} Number={:d} What={:s}'

x1 = 'sfdfs'
x2 = 15
x3 = 'p14'

print(pat.format(x1, x2, x3))