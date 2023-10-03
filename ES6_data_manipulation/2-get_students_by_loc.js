export default function getStudentsByLocation(getListStudents, city) {
  if (getListStudents instanceof Array) {
    const filterCity = getListStudents.filter((find) => find.location.includes(city));
    return filterCity;
  }
  return console.log('Il faut un tableau');
}
