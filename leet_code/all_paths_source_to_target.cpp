class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        return BFS(graph, 0);
    }
    
    vector<vector<int>> BFS(vector<vector<int>>& graph, int index) {
        vector<vector<int>> paths;
        paths.reserve(graph[index].size());
        if (graph[index].size() == 0) {
            vector<int> base{index};
            paths.push_back(base);
        }
        for (int next : graph[index]) {
            for (vector<int> new_path : this->BFS(graph, next)) {
                new_path.insert(new_path.begin(), index);
                paths.push_back(new_path);
            };
            
        }
        return paths;
    }
    
};