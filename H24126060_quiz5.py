grid_size = int(input("Enter the size of the gri:")) 

grid =[]  #形成一個size數量的"_"
i = 0
while i < grid_size**2:
	grid.append("_")
	i += 1

grid_str = "" #把grid分列
i = 0
while i < grid_size**2:
	row = grid[i:i+grid_size]
	grid_str += " ".join(row) + "\n"
	i += grid_size

print(grid_str)

coordinate = input("Enter the cell coordinates to edit:")
new_value = input("Enter the new value for the cell:")
coordinate_split = coordinate.split(",") #分成前後座標係數
value_added = []
while coordinate != "done": #回答不為done時算出座標數字，並加入value_added字串裡
	coordinate_number = grid_size*(int(coordinate_split[0]))+int(coordinate_split[1])
	if coordinate_number not in value_added:
		value_added.append(coordinate_number)

	grid =[] #如果座標數字已經有被輸入者輸入的話則填入輸入者想要的新值，沒有則填入"_"
	i = 0
	while i < grid_size**2:
		if i in value_added:
			grid.append(new_value)
		else:
			grid.append("_")
		i += 1

	grid_str = "" #分列
	i = 0
	while i < grid_size**2:
		row = grid[i:i+grid_size]
		grid_str += " ".join(row) + "\n"
		i += grid_size

	print(grid_str)