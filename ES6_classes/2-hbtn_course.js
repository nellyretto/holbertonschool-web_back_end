export default class HolbertonCourse {
  constructor(name, length, students) {
    /* eslint no-underscore-dangle: 0 */

    if (typeof (name) !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof (length) !== 'number') {
      throw TypeError('Length must be a number');
    }
    if (Array.isArray(students) === true && typeof (students[0]) !== 'string') {
      throw TypeError('Must be an array');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof (length) !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students) === true && typeof (students[0]) !== 'string') {
      throw TypeError('Must be an array');
    }
    this._students = students;
  }
}
