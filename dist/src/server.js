"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require('dotenv').config();
const express_1 = __importDefault(require("express"));
const body_parser_1 = __importDefault(require("body-parser"));
const subs_1 = __importDefault(require("./routes/subs"));
const DBindex_1 = __importDefault(require("./DBindex"));
const https_1 = __importDefault(require("https"));
const fs_1 = __importDefault(require("fs"));
const app = (0, express_1.default)();
const port = process.env.PORT;
DBindex_1.default.connect();
app.use(express_1.default.static('public'));
app.use(body_parser_1.default.json());
app.use(body_parser_1.default.urlencoded({ extended: true }));
const options = {
    ca: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/fullchain.pem'),
    key: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/privkey.pem'),
    cert: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/cert.pem'),
};
https_1.default.createServer(options, app).listen(port);
// app.use(
//   cors({
//     origin: 'http://localhost:3000',
//   }),
// );
app.use('/api', subs_1.default);
console.log(`
  ################################################
  🛡️  Server listening...
  ################################################
`);
//# sourceMappingURL=server.js.map