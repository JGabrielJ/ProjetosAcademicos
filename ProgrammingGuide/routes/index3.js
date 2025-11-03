var express = require('express');
var router = express.Router();
const { MongoClient } = require('mongodb');
var dataUsers = require('../src/dataUsers');

const uri = "mongodb+srv://JGabrielJ:YJ8p0KxoHQ5aMMEe@the-programming-guide-p.a0u75ny.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

router.post('/', async function(req, res, next) {
	try {
		await client.connect();

		const form = req.body;
		const ID = parseInt(form.userid);
		const USERNAME = form.username;
		const CHECKID = parseInt(form.checkid);

		if (ID != CHECKID) {
			res.send('<script> alert("Os IDs não correspondem!") </script>');
			return;
		}

		const result = await dataUsers.deleteUser(client, ID, USERNAME);
		res.redirect('/');
	} catch (err) {
		res.send(err);
	} finally {
		await client.close()
	}
});

module.exports = router;
