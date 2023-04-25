BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "roles" (
	"id"	VARCHAR(10) NOT NULL,
	"name"	VARCHAR(10) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	VARCHAR(10) NOT NULL,
	"email"	VARCHAR(30) NOT NULL,
	"_password"	VARCHAR(256) NOT NULL,
	"_salt"	VARCHAR(256) NOT NULL,
	"loginToken"	VARCHAR(10),
	UNIQUE("email"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "role-association_table" (
	"user_id"	VARCHAR(10) NOT NULL,
	"role_id"	VARCHAR(10) NOT NULL,
	FOREIGN KEY("role_id") REFERENCES "roles"("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("user_id","role_id")
);
INSERT INTO "roles" VALUES ('7cc49fcc-f749-4661-a6e1-519633247d64','user');
INSERT INTO "roles" VALUES ('7cc49fcc-f749-4661-a6e1-519633247d66','admin');
INSERT INTO "users" VALUES ('fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78','string4','0bfb02981511a79f43055fa1e7d880575518d91fbde7d2fb1283d27748c5b3192c14ce32c02eb0207f98485408a9b6dcbf3fe4329a11d86a520e0d0f3a5621e2','8a33cf83a2fc470bbffcbffc7bbf9cd9','27da2c7a-1523-4288-8e46-5781f36c8c92');
INSERT INTO "users" VALUES ('d0cacaa9-0f2e-4969-9ec9-0a771f5c0c02','string','89869d076b2f31781554d9a1cb923725bf528a653f4eaff7faae2fb2fb0385c31f95f0058559012898cd418e54eee790ae7e6f91a808cb0fb2a6878b6d8de41e','d09f547948ec45b692d90aa749905f8c','d8837096-c025-4ff0-8e75-839d32e51ec0');
INSERT INTO "role-association_table" VALUES ('fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78','7cc49fcc-f749-4661-a6e1-519633247d64');
INSERT INTO "role-association_table" VALUES ('d0cacaa9-0f2e-4969-9ec9-0a771f5c0c02','7cc49fcc-f749-4661-a6e1-519633247d64');
INSERT INTO "role-association_table" VALUES ('d0cacaa9-0f2e-4969-9ec9-0a771f5c0c02','7cc49fcc-f749-4661-a6e1-519633247d66');
COMMIT;
