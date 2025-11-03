var express = require('express');
var router = express.Router();
const { MongoClient } = require('mongodb');
var dataUsers = require('../src/dataUsers');
const session = require('express-session');

const uri = "mongodb+srv://JGabrielJ:YJ8p0KxoHQ5aMMEe@the-programming-guide-p.a0u75ny.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

router.use(session({
	secret: "myLittleSecretIsThatILoveYou<3",
	resave: false,
	saveUninitialized: true
}));

router.get('/', async function(req, res, next) {
	let user = req.session.user;
	const ID = (user) ? user.id : parseInt(req.query.id);

	try {
		await client.connect();

		const results = await dataUsers.readUser(client, ID);
		req.session.user = results[0];

		user = req.session.user;
		if (!user || user.id != ID) {
			res.send('<script> alert("Usuário não autenticado!"); </script>');
			return;
		}

		res.render('profile', { user: user });
	} catch (err) {
		res.send(err);
	} finally {
		await client.close()
	}
});

module.exports = router;
