# Given a valid (IPv4) IP address, return a defanged version of that IP address
# A defanged IP address replaces every period "." with "[.]".


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if i == '.' else i for i in address)


if __name__ == "__main__":
    print(Solution().defangIPaddr("192.168.1.1"))
