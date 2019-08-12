import java.util.List;


public class SlidingWindow {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new List<Integer>();
        int N = p.length();
        int diff = p.length();
        int start = 0, end = 0;

        if (s.length() == 0 || p.length() == 0 || s.length() < p.length()) {
            return res;
        }

        // create count of all the pattern
        int[] char_map = new int[26];
        for (char c : p.toCharArray()) {
            char_map[c - 'a']++;
        }

        while (end < N) {
            char c = s.charAt(end);
            char_map[c - 'a']--;
            if (char_map[c - 'a'] >= 0) {
                diff--;
            }
            end++;
        }

        if (diff == 0) res.add(0);

        while (end < s.length()) {
            char start_c = s.charAt(start);
            if (char_map[start_c - 'a'] >= 0) diff++;
            char_map[start_c - 'a']++;
            start++;

            char end_c = s.charAt(end);
            if (char_map[end_c - 'a'] >= 0) diff--;
            char_map[end_c - 'a']--;

            if (diff == 0) res.add(start);
            end++;
        }
    }
}