file1 = open('data\\Python_Introduction')
readme_txt = file1.read()
file1.close()
print type(readme_txt), len(readme_txt), readme_txt[:101]

with open('data\\Python_Introduction') as file2:
    readme_txt2 = file2.read().decode('UTF-8')
    readme_txt3 = file2.read().decode('ASCII')

print type(readme_txt2), len(readme_txt2), readme_txt2[:21]
print type(readme_txt3), len(readme_txt3), readme_txt3[:21]

file3 = open('data\\clone1','w')
file3.write(readme_txt)
file3.close()

with open('data\\clone2','w') as file4:
    file4.write(readme_txt2.encode('UTF-8'))

with open('data\\c2','w') as file5:
    file5.write(readme_txt2.encode('UTF-8'))