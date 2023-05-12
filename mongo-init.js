db = db.getSiblingDB('stcDb');

db.createUser(
        {
            user: "db_user",
            pwd: "db_password",
            roles: [
                {
                    role: "readWrite",
                    db: "stcDb"
                }
            ]
        }
);

db.createCollection('Users', {
        validator: {
        $jsonSchema: {
            bsonType: 'object',
                required: ['id', 'firstVisit', 'lastVisit'],
                properties: {
                    id: {
                        bsonType: 'int',
                        description: 'user id'
                    },
                    firstVisit: {
                        bsonType: 'date',
						description: 'first visit date'
					},
                    lastVisit: {
						bsonType: 'date',
						description: 'last visit date'
					}
                }
            }
	    }
    }
);