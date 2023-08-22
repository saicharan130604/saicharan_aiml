def can_finish(num_tasks, prerequisites):
    dependency_graph = [[] for _ in range(num_tasks)]
    visited = [False] * num_tasks
    in_degree = [0] * num_tasks
    start_node = -1
    
    for prerequisite in prerequisites:
        task, dependency = prerequisite
        dependency_graph[dependency].append(task)
        in_degree[task] += 1
    
    for i in range(num_tasks):
        if in_degree[i] == 0:
            start_node = i
    
    if start_node == -1:
        return False
    else:
        def depth_first_search(node):
            visited[node] = True
            for neighbor in dependency_graph[node]:
                if not visited[neighbor]:
                    if not depth_first_search(neighbor):
                        return False
                else:
                    return False
            return True
    
    return depth_first_search(start_node)

print(can_finish(4, [[0, 1], [1, 2], [2, 3], [3, 0]])) 
print(can_finish(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(can_finish(3, [[0, 1], [1, 2], [2, 0]]))
print(can_finish(6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]])) 
print(can_finish(3, [[1, 0], [2, 1], [0, 2]]))  
