var express = require('express');
var router = express.Router();
const { MongoClient } = require('mongodb');
var dataUsers = require('../src/dataUsers');

const uri = "mongodb+srv://JGabrielJ:YJ8p0KxoHQ5aMMEe@the-programming-guide-p.a0u75ny.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

router.post('/', async function(req, res, next) {
	const form = req.body;
	const ID = parseInt(form.userid);

	try {
		await client.connect();

		const result = await dataUsers.checkUser(client, ID);
		if (!result) {
			res.send('<script> alert("O usuário não existe!"); </script>');
			return;
		}

		res.redirect(`/profile?id=${ID}`);
	} catch (err) {
		res.send(err);
	} finally {
		await client.close()
	}
});

module.exports = router;
