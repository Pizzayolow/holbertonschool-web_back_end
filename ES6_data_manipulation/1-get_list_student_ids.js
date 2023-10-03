export default function getListStudentIds(getListStudents) {
  const emptyArray = [];
  if (getListStudents instanceof Array) {
    const ids = getListStudents.map((students) => students.id);
    return ids;
  }
  return emptyArray;
}
