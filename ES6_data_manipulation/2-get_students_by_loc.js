export default function getStudentsByLocation(getListStudents, city) {
  const filterCity = getListStudents.filter((find) => find.location.includes(city));
  return filterCity;
}
