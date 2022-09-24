"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require('dotenv').config();
const express_1 = __importDefault(require("express"));
const subs_1 = __importDefault(require("../controllers/subs"));
const router = express_1.default.Router();
router.post('/subscription', subs_1.default.register);
exports.default = router;
//# sourceMappingURL=subs.js.map