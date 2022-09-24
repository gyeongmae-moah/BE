"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require('dotenv').config();
const DBindex_1 = __importDefault(require("../DBindex"));
const register = (req, res) => {
    const { email, gender, age } = req.body;
    if (!CheckEmail(email))
        return res.status(400).json({
            result: false,
            err_code: 400,
            detail: '이메일 형식 에러',
        });
    // 이메일이 NULL인 경우 예외 처리
    if (!email)
        return res.status(400).json({
            result: false,
            err_code: 400,
            detail: '이메일 NULL 에러',
        });
    try {
        // 중복 이메일 확인
        DBindex_1.default.query('select email from user where email=?', email, (error, result) => {
            if (result[0])
                return res.status(400).json({
                    result: false,
                    err_code: 400,
                    detail: '이메일 중복 에러',
                });
            const query = 'insert into user(email, gender, age, date) values(?, ?, ?, date_format(curdate(), "%Y-%m-%d"))';
            const value = [email, gender, age];
            DBindex_1.default.query(query, value, (error) => {
                if (error)
                    return res.status(400).json({
                        result: false,
                        err_code: 400,
                        detail: 'sql 에러',
                    });
                console.log('구독 등록: ', email);
                return res.status(200).json({
                    result: true,
                });
            });
        });
    }
    catch (error) {
        return res.status(400).json({
            result: false,
            err_code: 400,
            detail: '캐치 에러',
        });
    }
};
function CheckEmail(email) {
    const reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
    if (!reg_email.test(email))
        return false;
    return true;
}
exports.default = { register };
//# sourceMappingURL=subs.js.map