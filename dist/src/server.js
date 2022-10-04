"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require('dotenv').config();
const express_1 = __importDefault(require("express"));
const body_parser_1 = __importDefault(require("body-parser"));
const cors_1 = __importDefault(require("cors"));
const subs_1 = __importDefault(require("./routes/subs"));
const DBindex_1 = __importDefault(require("./DBindex"));
const https_1 = __importDefault(require("https"));
const fs_1 = __importDefault(require("fs"));
const express_rate_limit_1 = __importDefault(require("express-rate-limit"));
const helmet_1 = __importDefault(require("helmet"));
const app = (0, express_1.default)();
const port = process.env.PORT;
DBindex_1.default.connect();
app.use((0, helmet_1.default)());
app.use(express_1.default.static('public'));
app.use(body_parser_1.default.json());
app.use(body_parser_1.default.urlencoded({ extended: true }));
const options = {
    ca: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/fullchain.pem'),
    key: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/privkey.pem'),
    cert: fs_1.default.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/cert.pem'),
};
app.use((0, express_rate_limit_1.default)({
    windowMs: 1 * 60 * 1000,
    max: 100,
}));
app.use((0, cors_1.default)({
    origin: 'https://gmmoa.com',
}));
app.get('/', (req, res) => {
    return res.status(400).send('<script>alert("올바르지 않은 접근입니다.")</script>');
});
app.use('/api', subs_1.default);
https_1.default.createServer(options, app).listen(port, () => {
    console.log(`
  ################################################
    서버 연결 성공 !
  ################################################
`);
});
//# sourceMappingURL=server.js.map