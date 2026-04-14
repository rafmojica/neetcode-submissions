class Solution {
    public boolean isValid(String s) {
        // a stack is valid here because we can track
        // the last open bracket. 
        // it must be closed with the same bracket.
        
        Map<Character, Character> closeP = Map.of(')', '(', ']', '[', '}', '{');
        List<Character> stack = new ArrayList<>();
        // s = (([]))
        // stack = (([

        // the most recent open parenthesis must be closed.
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (closeP.containsKey(c)) {
                if (!stack.isEmpty() && stack.get(stack.size() - 1).equals(closeP.get(c))) {
                    stack.remove(stack.size() - 1);
                } else {
                    return false;
                }
            } else {
                stack.add(s.charAt(i));
            }
        }

        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}
