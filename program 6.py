print('Anas Ahmed')
print('LAb 11, 18B-116-cs, Program 06\n')

My_topStudents = {'Bassam','Usman','Rafeh', 'Ahad', 'Wadood','Yusra',
'Asma'}
print('My top scoring students in Programming fundamentals are:',My_topStudents)
print('Oh, I guess I miss one student, let me add his name too')
print('Previously I have added :'+ str(len(My_topStudents)) +'students in my list')
My_topStudents.add('Khurram Khalil')
My_topStudents.add('Khurram Khan')
print('Thanks, I have remember him')
print('Now my top scoring students names are :', My_topStudents)
print('Now after adding I have :'+ str(len(My_topStudents)) +'students in my list')
print('Oh, I guess I have added one student with similar name, let meremove his name.')
My_topStudents.remove('Khurram Khalil')
print('Now my top scoring students names after removing extra name are:', My_topStudents)
print('Now after removing I have :'+ str(len(My_topStudents)) +'students in my list')
