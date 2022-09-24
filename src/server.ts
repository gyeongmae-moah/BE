require('dotenv').config();
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import subs_router from './routes/subs';
import db from './DBindex';

const app = express();

db.connect();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(
  cors({
    origin: 'http://localhost:3000',
  }),
);

app.use('/api', subs_router);

const port = process.env.PORT;

app.listen(port, () => {
  console.log(`
  ################################################
  🛡️  Server listening...
  ################################################
`);
});
