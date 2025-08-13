const functions = require("firebase-functions/v2/https");
const { onRequest } = functions;
const threatAgent = require("./threatAgentFunction");

exports.analyzeThreat = onRequest(threatAgent);
