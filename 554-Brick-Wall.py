class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        row_edge_map ={}
        for row in range(len(wall)):
            edge_position =0
            for edge in range(len(wall[row])-1):
                edge_position += wall[row][edge]
                row_edge_map[edge_position] = row_edge_map.get(edge_position, 0) + 1
        return len(wall) - max(row_edge_map.values(), default =0)