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
const app = (0, express_1.default)();
DBindex_1.default.connect();
app.use(express_1.default.static('public'));
app.use(body_parser_1.default.json());
app.use(body_parser_1.default.urlencoded({ extended: true }));
// app.use(
//   cors({
//     origin: 'http://localhost:3000',
//   }),
// );
app.use('/api', subs_1.default);
const port = process.env.PORT;
app.listen(port, () => {
    console.log(`
  ################################################
  🛡️  Server listening...
  ################################################
`);
});
//# sourceMappingURL=server.js.map