export default function getListStudents() {
  const array = [];

  const object = { id: 1, firstName: 'Guillaume', location: 'San Francisco' };
  const object2 = { id: 2, firstName: 'James', location: 'Columbia' };
  const object3 = { id: 5, firstName: 'Serena', location: 'San Francisco' };
  array.push(object, object2, object3);
  return array;
}
