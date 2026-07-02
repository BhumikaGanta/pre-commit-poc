// src/models/sampleModel.js
class SampleModel {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }
}

// Example data
const sampleData = [
  new SampleModel(1, "Sample Item 1"),
  new SampleModel(2, "Sample Item 2"),
];

module.exports = sampleData;
