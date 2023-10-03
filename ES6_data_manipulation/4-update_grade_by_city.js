function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: matchingGrade ? matchingGrade.grade : 'N/A',
      };
    });
}

export default updateStudentGradeByCity;
