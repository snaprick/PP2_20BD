class Solution:
    def interpret(self, command: str) -> str:
        s = command.replace("()","o")
        s = s.replace("(al)","al")
        return s