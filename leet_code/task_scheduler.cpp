#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char> & tasks, int n) {
        // use sorted int array to move all actual tasks to end
        // and A - Z tasks for array of size 26
        int task_map[26] = {0};
        for (char c: tasks) ++task_map[c - 'A'];
        int intervals = 0;
        sort(task_map, task_map+26);
        
        // the returned task list doesn't actually matter, 
        // just the number of intervals
        //just iterate backwards from end and once reach point where
        // no more tasks at that index, just loop again and
        // increase interval count, doesn't matter how many in-between
        // idle times there are, rather just that we are doing another interval
        while (task_map[25] > 0) {
            int i = n;
            while (i > 0) {
                
            }
            // sort again to ensure most abundant task is completed first since 
            // it's the main factor for determining number of intervals
            sort(task_map, task_map+26);
        }
        return intervals;

    }
};