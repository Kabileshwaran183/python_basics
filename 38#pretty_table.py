import prettytable
table = prettytable.PrettyTable()
table.add_column("name",["kabi","arun","vimala"])
table.add_column("age",["19","24","16"])

table.align ="l"
print(table)