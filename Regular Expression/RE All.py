# import re

 # # # # # text = "My age is 21 and my number is 9876543210"
# # # # # result = re.findall(r'\d', text)

# # # print("Digits:", result)




# # # # # # # # # # # # import re
# # # # # # # # # # # # # Imports regular expression module

# # # # # # # # # # # # text = "An apple and a mango are amazing"
# # # # # # # # # # # # # Stores a sentence

# # # # # # # # # # # # result = re.findall(r'\b[Aa]\w*', text)
# # # # # # # # # # # # # Finds words starting with A or a

# # # # # # # # # # # # print("Words:", result)
# # # # # # # # # # # # # Displays matching words




# # # # # # # # # # # import re
# # # # # # # # # # # # Imports regular expression module

# # # # # # # # # # # text = "Hello World"
# # # # # # # # # # # # Stores a string

# # # # # # # # # # # result = re.findall(r'[aeiouAEIOU]', text)
# # # # # # # # # # # # Finds all vowels

# # # # # # # # # # # print("Vowels:", result)
# # # # # # # # # # # # Displays vowels

# # # # # # # # # # # print("Total Vowels:", len(result))
# # # # # # # # # # # # Counts total vowels
















# # # # # # # # # # import re
# # # # # # # # # # # Imports regular expression module

# # # # # # # # # # text = "Hello PYTHON World"
# # # # # # # # # # # Stores a string

# # # # # # # # # # result = re.findall(r'[A-Z]', text)
# # # # # # # # # # # Finds all uppercase letters

# # # # # # # # # # print("Uppercase Letters:", result)
# # # # # # # # # # # Displays uppercase letters








# # # # # # # # # import re
# # # # # # # # # # Imports regular expression module

# # # # # # # # # text = "Hello World\nPython\tProgramming"
# # # # # # # # # # Stores text containing space, newline and tab

# # # # # # # # # result = re.findall(r'[ \t\n]', text)
# # # # # # # # # # Finds spaces, tabs and newline characters

# # # # # # # # # print("Characters:", result)
# # # # # # # # # # Displays matching characters

# # # # # # # # # print("Total:", len(result))
# # # # # # # # # # Counts matching characters















# # # # # # # # import re
# # # # # # # # # Imports regular expression module

# # # # # # # # text = "Python    is     very   easy"
# # # # # # # # # Stores a string with multiple spaces

# # # # # # # # result = re.sub(r' +', ' ', text)
# # # # # # # # # Replaces multiple spaces with one space

# # # # # # # # print(result)
# # # # # # # # # Displays the modified string












# # # # # # # import re
# # # # # # # # Imports regular expression module

# # # # # # # text = "Apple mango grape hello world"
# # # # # # # # Stores a sentence

# # # # # # # result = re.findall(r'\b\w{5}\b', text)
# # # # # # # # Finds words containing exactly five characters

# # # # # # # print("Five Character Words:", result)
# # # # # # # # Displays matching words





# # # # # # import re
# # # # # # # Imports regular expression module

# # # # # # text = "Ravi likes apples and bananas"
# # # # # # # Stores a sentence

# # # # # # result = re.findall(r'\b\w+s\b', text)
# # # # # # # Finds words ending with s

# # # # # # print("Words:", result)
# # # # # # # Displays matching words









# # # # # import re
# # # # # # Imports regular expression module

# # # # # text = "Hello@ Python#123! Welcome."
# # # # # # Stores a string containing special characters

# # # # # result = re.sub(r'[^A-Za-z0-9 ]', '', text)
# # # # # # Removes special characters and keeps letters, digits and spaces

# # # # # print(result)
# # # # # # Displays the final string














# # # # import re
# # # # # Imports regular expression module

# # # # text = "Python is an easy programming language"
# # # # # Stores a sentence

# # # # result = re.findall(r'\b\w+\b', text)
# # # # # Finds all words

# # # # print("Words:", result)
# # # # # Displays all words

# # # # print("Total Words:", len(result))
# # # # # Counts total words







# # # import re
# # # # Imports regular expression module

# # # number = input("Enter mobile number: ")
# # # # Accepts mobile number from user

# # # if re.fullmatch(r'[6-9]\d{9}', number):
# # #     # Checks whether number has 10 digits and starts from 6 to 9
# # #     print("Valid Mobile Number")
# # #     # Displays valid message

# # # else:
# # #     # Executes when number is incorrect
# # #     print("Invalid Mobile Number")
# # #     # Displays invalid message



















# # import re
# # # Imports regular expression module

# # email = input("Enter email: ")
# # # Accepts email from user

# # pattern = r'^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$'
# # # Defines the email format

# # if re.fullmatch(pattern, email):
# #     # Checks whether email matches the pattern
# #     print("Valid Email")
# #     # Displays valid message

# # else:
# #     # Executes when email is incorrect
# #     print("Invalid Email")
# #     # Displays invalid message






# # import re
# # # Imports regular expression module

# # text = "My birthday is 15-08-2004 and admission date is 10-06-2025"
# # # Stores a paragraph containing dates

# # result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
# # # Finds dates in DD-MM-YYYY format

# # print("Dates:", result)
# # # Displays extracted dates












# import re
# # Imports regular expression module

# text = "Visit https://google.com and http://example.com"
# # Stores a sentence containing web addresses

# result = re.findall(r'https?://[^\s]+', text)
# # Finds addresses starting with http or https

# print("Web Addresses:", result)
# # Displays web addresses



# import re
# # Imports regular expression module

# text = "Enjoying #Python and #Programming today #Learning"
# # Stores a social media post

# result = re.findall(r'#[A-Za-z0-9_]+', text)
# # Finds all hashtags

# print("Hashtags:", result)
# # Displays hashtags