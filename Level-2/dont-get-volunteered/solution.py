def solution(src, dest):
    # all possible directions the knight can move
    possible_moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

    # check if src and dest in bounds
    if src < 0 or src >= 64 or dest < 0 or dest >= 64:
        return 0

    # if src and dest are same return 0
    if src == dest:
        return 0

    # convert src and dest to cartesian system
    src = (src//8, src%8)
    dest = (dest//8, dest%8)

    queue = list()
    queue.append(src)

    visited = [[False for _ in range(9)] for _ in range(9)]
    current_moves = 0

    # bfs to find the dest starting from src
    while len(queue) > 0:
        # make a copy of the current queue state
        current_queue = queue.copy()

        for pos in current_queue:
            current = pos
            queue.pop(0) # remove current cell from queue

            visited[current[0]][current[1]] = True # set current cell visited status to true

            for move in possible_moves:
                new_place = (current[0]+move[0], current[1]+move[1]) # new cell to visit next
                new_place_integer = new_place[0]*8 + new_place[1] # convert to integer to check out of bounds
                if new_place_integer < 0 or new_place_integer >= 64:
                    continue
                elif new_place == dest:
                    return current_moves+1
                else:
                    if not visited[new_place[0]][new_place[1]]: # prevent duplication of computing if cell is visited
                        queue.append(new_place) # add new cell to the queue
        current_moves += 1

    return 0

if __name__ == '__main__':
    print(solution(19, 36))
    print(solution(0, 1))


