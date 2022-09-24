require('dotenv').config();
import express from 'express';
import subs_controller from '../controllers/subs';

const router = express.Router();

router.post('/subscription', subs_controller.register);

export default router;
