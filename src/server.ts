require('dotenv').config();
import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import subs_router from './routes/subs';
import db from './DBindex';
import https from 'https';
import fs from 'fs';
import express_rate_limit from 'express-rate-limit';
import helmet from 'helmet';
import csp from 'helmet-csp';

const app = express();
const port = process.env.PORT;

db.connect();

app.use(helmet());
app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// app.use(
//   csp({
//     directives: {
//       scriptSrc: ["'self'", 'gmmoa.com'],
//     },
//   }),
// );

const options = {
  ca: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/fullchain.pem'),
  key: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/privkey.pem'),
  cert: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/cert.pem'),
};

app.use(
  express_rate_limit({
    windowMs: 1 * 60 * 1000,
    max: 100,
  }),
);

app.use(
  cors({
    origin: 'http://localhost:3000',
  }),
);

app.get('/', (req: Request, res: Response) => {
  return res.status(200).send('<script unsafe-inline>alert("올바르지 않은 접근입니다.")</script>');
});

app.use('/api', subs_router);

https.createServer(options, app).listen(port, () => {
  console.log(`
  ################################################
    서버 연결 성공 !
  ################################################
`);
});
