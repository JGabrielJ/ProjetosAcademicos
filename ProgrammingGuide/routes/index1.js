var express = require('express');
var router = express.Router();
const { MongoClient } = require('mongodb');
var dataUsers = require('../src/dataUsers');

const uri = "mongodb+srv://JGabrielJ:YJ8p0KxoHQ5aMMEe@the-programming-guide-p.a0u75ny.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

function random(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

router.post('/', async function(req, res, next) {
	const form = req.body;
	let ID = random(0, 9999);
	let notOK = true;

	try {
		await client.connect();

		while (notOK) {
			const result = await dataUsers.checkUser(client, ID);
			if (result) {
				ID = random(0, 9999);
			} else {
				notOK = false;
			}
		}

		const userData = {
			id: ID,
			username: form.usuario,
			name: form.nome,
			description: "",
			birthday: form.data,
			email: form.e_mail,
			image: "./images/profile.png"
		};

		const newUser = await dataUsers.createUser(client, userData);
		res.redirect(`/profile?id=${userData.id}`);
	} catch (err) {
		res.send(err);
	} finally {
		await client.close()
	}
});

module.exports = router;
