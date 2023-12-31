export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // getters and setters
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof (newName) === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('TypeError: Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof (newLength) === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('TypeError: Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudent) {
    if (
      Array.isArray(newStudent)
            && newStudent.every((student) => typeof student === 'string')
    ) {
      this._students = newStudent; // Initialisez l'attribut underscore _students
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
