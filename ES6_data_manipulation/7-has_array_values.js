export default function hasValuesFromArray(set, array) {
  const setArray = [...set];
  for (const data of array) {
    if (!setArray.includes(data)) {
      return false;
    }
  }
  return true;
}
