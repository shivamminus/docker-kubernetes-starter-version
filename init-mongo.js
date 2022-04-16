db = db.getSiblingDB('mypydb')
db.createUser({ user: "mongodbshivam", pwd: "mypwdformongodb", roles: [{ role: "readWrite", db: "mypydb" }] })
