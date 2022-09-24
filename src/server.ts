require('dotenv').config();
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import subs_router from './routes/subs';
import db from './DBindex';
import https from 'https';
import * as fs from 'fs';

const app = express();
const port = process.env.PORT;

db.connect();

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const options = {
  ca: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/fullchain.pem'),
  key: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/privkey.pem'),
  cert: fs.readFileSync('/etc/letsencrypt/live/api.gmmoa.com/cert.pem'),
};
https.createServer(options, app).listen(port);

// app.use(
//   cors({
//     origin: 'http://localhost:3000',
//   }),
// );

app.use('/api', subs_router);

console.log(`
  ################################################
  🛡️  Server listening...
  ################################################
`);
