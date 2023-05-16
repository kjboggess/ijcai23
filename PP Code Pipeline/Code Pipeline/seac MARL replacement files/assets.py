#Adpated From: Semitable and Trevor McInroe
#Original Code Location: https://github.com/semitable/pressureplate

"""
	For ease of use, please lay out your grid in Euclidean-plane format and NOT
	in numpy-type format. For example, if an object needs to be placed in the
	3rd row and 7th column of the gridworld numpy matrix, enter its location in your
	layout dict as [7,3]. The codebase will take care of the matrix-indexing for you.
	For example, the above object will be queried as grid[3, 7] when placed into the
	grid.
	NOTE: the origin (0,0) is the top-left corner of the grid. The positive direction
	along the x-axis counts to the right and the positive direction along the y-axis
"""
LINEAR = {
	'FOUR_PLAYER_WALLS': [
		# First wall
		[0, 11],
		[1, 11],
		[2, 11],
		[3, 11],
		[4, 11],
		[5, 11],
		[8, 11],

		# Second wall
		[0, 7],
		[1, 7],
		[4, 7],
		[5, 7],
		[6, 7],
		[7, 7],
		[8, 7],

		 #Third wall
		[0, 3],
		[1, 3],
		[2, 3],
		[3, 3],
		[4, 3],
		[5, 3],
		[8, 3],

        #4th Wall
        [0, 2],
		[1, 2],
		[2, 2],
		[3, 2],
		[4, 2],
		[5, 2],
		[8, 2],

	],

	# Doors are double doors of coord [[x1,x2], [y1,y2]]
	'FOUR_PLAYER_DOORS': [
		[[6, 7], [11, 11]],
		[[2, 3], [7, 7]],
		[[6, 7], [3, 3]],
        [[6, 7], [2, 2]],
	],

	'FOUR_PLAYER_PLATES': [
		[2, 13],
		[7, 13],
		[2, 9],
		[7, 9],
		[7, 5],
		[2, 5],
        [8, 6],
        [1, 6],

	],

	'FOUR_PLAYER_AGENTS': [
		[5, 13], # [5, 13],
		[5, 12],
		[4, 13],
		[4, 12],
		[3, 12],
		[3, 13],
		[2, 12],
        [1, 12],
        [1, 13]
	],

	'FOUR_PLAYER_GOAL': [
		[3, 1]
	]
}
