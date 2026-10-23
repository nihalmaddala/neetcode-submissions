class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Convert characters to numbers, separated by space
            ascii_word = " ".join(str(ord(char)) for char in s)
            # Add a COMMA at the end of every word to mark its boundary
            res += ascii_word + ","
        return res

    def decode(self, s: str) -> List[str]:
        # Edge case: if the original list was completely empty (strs = [])
        if not s: 
            return [] 
            
        arr = []
        # Split by comma. We use [:-1] because our encoded string ends with a comma, 
        # which creates a blank leftover item at the very end of the split list.
        encoded_words = s.split(',')[:-1]
        
        for word in encoded_words:
            # Edge case: if the word itself was an empty string (strs = [""])
            if word == "":
                arr.append("")
            else:
                temp = "".join(chr(int(num)) for num in word.split(' '))
                arr.append(temp)
                
        return arr