// src/controllers/sampleController.js
const sampleData = require("../models/sampleModel");

const getAllSamples = (req, res) => {
  res.json(sampleData);
};

module.exports = {
  getAllSamples,
};
