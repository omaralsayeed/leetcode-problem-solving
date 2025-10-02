#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> freq;

        // Count frequency of each char
        for (char c : s) {
            freq[c]++;
        }

        // All frequencies must be equal
        int expected = freq.begin()->second;
        for (auto &p : freq) {
            if (p.second != expected) return false;
        }

        return true;
    }
};
