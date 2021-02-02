class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = address.replace(".","[.]")
        return s