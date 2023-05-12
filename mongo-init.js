db.getSiblingDB('stcDb');

db.createCollection(
    'Users', {
        id: <string>,
        firstVisit: <string>,
        lastVisit: <string>
    }
);

