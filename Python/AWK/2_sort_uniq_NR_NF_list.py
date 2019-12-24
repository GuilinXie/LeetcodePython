# print NR, row number
cat file | awk -F ' ' '{print NR}'

# print NF, column number
cat file | awk -F ' ' '{print NF}'

# sort, uniq, count
# sort -k2 : This will sort alphabetically based on the 2nd column
cat file | awk -F ' ' '{print $2}' | sort | uniq -c | sort -nr

'''
reference:
http://blog.chinaunix.net/uid-10540984-id-1185098.html
'''
# $2+$3 to be a new column $5
# avg($5)
# count how many rows in $5 > avg($5)

# method 1
awk '{x+=$2+$3;a[NR]=$2+$3}END{y=x/NR;for(i in a){if(y<a[i])z++} print z}' file

# method 2
awk 'BEGIN{while(getline<"file'){x+=$2+$3;i++};y=x/i}{if($2+$3>y)z++}END{print z}' file

# 1st col in file2, but 1st col not file1：
awk 'BEGIN{while(getline<"file1"){a[$1]=1}}{if(a[$1]!=1)print $1}' file2

# sort
cat n.txt | sort -n   # ascending order by number
cat n.txt | sort -nr  # descending order by number
cat n.txt | sort      # ascending order by string
cat n.txt | sort -r   # descending order by string
cat facebook.txt | sort -n -t ' ' -k 2 -k 3    # number, ' ' separator , 2nd col ascending, 3rd col ascending
cat facebook.txt | sort -n -t ' ' -k 2r -k 3   # number, ' ' separator , 2nd col descending, 3rd col ascending
