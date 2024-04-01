student = {
  'name': 'Urvi',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Urvi'})
print(student.keys() >= {'roll_id', 'name'}) 
