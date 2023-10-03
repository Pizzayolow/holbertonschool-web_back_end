export default function getStudentIdsSum(getListStudents) {
  const sum = getListStudents.reduce((total, data) => total + data.id, 0);
  return sum;
}
