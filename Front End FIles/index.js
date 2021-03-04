let crypto = require("crypto");
let sha1 = crypto.createHash("sha1").update("April18-0418").digest("hex");
console.log(sha1);
let sha256 = crypto.createHash("sha256").update("April18-0418").digest("hex")
console.log(sha256)