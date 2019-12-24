'''
reference: https://blog.csdn.net/qingsong3333/article/details/79647933
implement a similar function as group by in SQL

income.txt
Jan 100
March   200
April   210
Jan 200
April   220
Jan 300
'''

awk '{a[$1]+=$2} END{for(mon in a) printf("%s\t\t%s\n",mon,a[mon])}' income.txt | sort -n -k2r

'''
output:
Jan 600
April 430
March 200
'''

