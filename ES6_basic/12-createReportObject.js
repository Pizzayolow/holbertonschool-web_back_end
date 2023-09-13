/* eslint-disable */
export default function createReportObject(employeesList) {
  let count = 0;
  const all = {
    getNumberOfDepartments(employeesList) {
      for (const department in employeesList) {
        count++;
      }
      return (count);
    },
    allEmployees: employeesList,
  };
  return (all);
}
