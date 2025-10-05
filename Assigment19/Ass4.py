num = input("Enter the input:")
vowels = 'AEIOUaeiou'
result =''.join([i for i in num if i not in vowels])
print('string removes vowels:',result)

