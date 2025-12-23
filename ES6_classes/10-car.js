export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Symbol.species tells JS which constructor to use when cloning
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Cls = this.constructor[Symbol.species];
    return new Cls();
  }
}
