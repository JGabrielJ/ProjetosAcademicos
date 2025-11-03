class DataUsers {
    static async checkUser(client, ID) {
        try {
            let idArray = [];

            const cursor = await client
                .db('usersData')
                .collection('usuarios')
                .find({})
                .project({ _id: 0, username: 0, name: 0, description: 0, birthday: 0, email: 0, image: 0 });

            const results = await cursor.toArray();
            results.forEach(result => {
                idArray.push(result.id);
            });

            if (idArray.includes(ID)) {
                return true
            } else {
                return false
            }
        } catch (err) {
            console.log(err);
        }
    }

    static async createUser(client, user) {
        try {
            const result = await client
            .db('usersData')
            .collection('usuarios')
            .insertOne(user);

            return result;
        } catch (err) {
            console.log(err);
        } finally {
            await client.close()
        }
    }

    static async readUser(client, ID) {
        try {
            const results = await client
            .db('usersData')
            .collection('usuarios')
            .find({ id: ID })
            .project({ _id: 0 });

            return await results.toArray();
        } catch (err) {
            console.log(err);
        } finally {
            await client.close()
        }
    }

    static async updateUser(client, ID, doc) {
        try {
            const filter = { id: ID };
            const newValues = {
                $set: {
                    name: doc.name,
                    description: doc.description,
                    birthday: doc.birthday,
                    email: doc.email,
                    image: doc.image
                }
            };

            const result = await client
            .db('usersData')
            .collection('usuarios')
            .updateOne(filter, newValues);

            return result;
        } catch (err) {
            console.log(err);
        }
    }

    static async deleteUser(client, ID, USERNAME) {
        try {
            const result = await client
            .db('usersData')
            .collection('usuarios')
            .deleteOne({ id: ID, username: USERNAME });

            return result;
        } catch (err) {
            console.log(err);
        } finally {
            await client.close()
        }
    }
}

module.exports = DataUsers;
