#include <unordered_map>

class Solution {
public:
    char prev_char = '\0';
    string reorganizeString(string s) {
        unordered_map<char, int> umap;

        string result = "";

        for (int i = 0; i < s.size(); i++) {
            if (umap.contains(s[i])) {
                umap[s[i]] += 1;
            } else {
                umap[s[i]] = 1;
            }
        }

        for (auto pair: umap) {
            std::cout << pair.first << " " << pair.second << "\n";
        }

        while (umap.size() > 0) {
            int max = 0;
            int max2 = 0;
            char chr = '\0';
            char chr2 = '\0';

            for (auto pair: umap) {
                if (pair.second > max) {
                    max2 = max;
                    chr2 = chr;
                    max = pair.second;
                    chr = pair.first;
                    
                } else if (pair.second > max2) {
                    max2 = pair.second;
                    chr2 = pair.first;
                }
            }

            if (prev_char != chr) {
                result += chr;
                umap[chr] -= 1;
                if (umap[chr] == 0) {
                    umap.erase(chr);
                }
                prev_char = chr;
            } else if (max2 != 0) {
                result += chr2;
                umap[chr2] -= 1;
                if (umap[chr2] == 0) {
                    umap.erase(chr2);
                }
                prev_char = chr2;
            } else {
                return "";
            }
        }
        return result;
    }
};
