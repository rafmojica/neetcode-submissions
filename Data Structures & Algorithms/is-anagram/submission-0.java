class Solution {
    public boolean isAnagram(String s, String t) {
        // store each character of s in a hashmap
        // store each character of t in a hashmap
        // compare if both hashmaps contains the same values
        Map<Character, String> sHashMap = new HashMap<>();
        Map<Character, String> tHashMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            sHashMap.put(s.charAt(i), sHashMap.get(s.charAt(i)) + 1);
        }
        for (int j = 0; j < t.length(); j++) {
            tHashMap.put(t.charAt(j), tHashMap.get(t.charAt(j)) + 1);
        }

        if (sHashMap.equals(tHashMap))
            return true;
        else
            return false;
    }
}
