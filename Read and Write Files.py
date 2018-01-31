# Create File sample.txt
fw = open('sample.txt', 'w')
fw.write('Writing Stuff in my text file\n')
fw.write('Hello this is a new file created\n')
fw.close() #Close file object



# Read File sample.txt
fr = open('sample.txt', 'r')

# store data from File sample.txt
text = fr.read()
print(text)
fr.close()

'''
Screen print out
Writing Stuff in my text file
Hello this is a new file created
'''
