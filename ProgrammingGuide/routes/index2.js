var express = require('express');
var router = express.Router();
const { MongoClient } = require('mongodb');
var dataUsers = require('../src/dataUsers');
const multer = require('multer');

const uri = "mongodb+srv://JGabrielJ:YJ8p0KxoHQ5aMMEe@the-programming-guide-p.a0u75ny.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

const storage = multer.diskStorage({
	destination: function(req, file, cb) {
	  	cb(null, './public/images/profiles');
	},

	filename: function(req, file, cb) {
	  	cb(null, file.originalname);
	}
});

const upload = multer({ storage: storage });

router.post('/', upload.single('profile'), async function(req, res, next) {
	const form = req.body;
	const ID = parseInt(req.query.id);
	const doc = {
		name: form.name,
		description: form.desc,
		birthday: form.date,
		email: form.email,
		image: req.file ? `./images/profiles/${req.file.filename}` : "./images/profile.png"
	};

	try {
		await client.connect();
		const result = await dataUsers.updateUser(client, ID, doc);
		res.redirect(`/profile?id=${ID}`);
	} catch (err) {
		res.send(err);
	} finally {
		await client.close()
	}
});

module.exports = router;
