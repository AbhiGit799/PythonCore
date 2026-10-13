
'''

Remember these three things:

str(count) converts the number into a string.

digit takes one character at a time.

write += 1 moves to the next position in the list.


3. Why do we need this loop?
******************************
Imagine the input contains 12 consecutive "a" characters.

The compressed output should be:

["a", "1", "2"]

Not:

["a", 12]

Because the problem requires each digit of the count to be stored as a separate character.

'''

count = 12
print(str(count)) # This converts the integer count to a string and prints it.

chars = ["a", "a", "a", "a", "a", "a"]
write = 1

for digit in str(count):
    chars[write] = digit
    write += 1

print(chars)

class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        i = 0 
        while i < len(chars):
            char = chars[i]
            count = 0
            while i<len(chars) and chars[i]==char:
                i=i+1
                count = count + 1
            chars[write] = char
            write = write + 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write = write + 1   
        return write

obj = Solution()
chars = ["a", "a", "a", "a", "a", "a"]
length = obj.compress(chars)
print(length)  # This will print the new length of the compressed list.



                









