def table_print(table):
    index_max_length = {}
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if j not in index_max_length:
                index_max_length[j] = len(tableData[i][j])
            else:
                if len(tableData[i][j]) > index_max_length[j]:
                    index_max_length[j] = len(tableData[i][j])
    pretty_table = ''
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            pretty_table += str(tableData[i][j]).rjust(index_max_length[j]) 
            if j != len(tableData[i]) - 1: pretty_table += ' '
    print(pretty_table)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
table_print(tableData)
