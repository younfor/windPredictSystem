PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2015-03-10 09:25:31.830047');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2015-03-10 09:25:32.079268');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2015-03-10 09:25:32.338606');
INSERT INTO "django_migrations" VALUES(4,'sessions','0001_initial','2015-03-10 09:25:32.609211');
INSERT INTO "django_migrations" VALUES(5,'wind','0001_initial','2015-03-10 09:25:32.992111');
INSERT INTO "django_migrations" VALUES(6,'wind','0002_auto_20150310_0924','2015-03-10 09:25:34.121714');
INSERT INTO "django_migrations" VALUES(7,'wind','0003_userprofile_father','2015-01-15 10:08:29.168057');
INSERT INTO "django_migrations" VALUES(8,'wind','0004_auto_20150109_0725','2015-01-15 10:08:29.504145');
INSERT INTO "django_migrations" VALUES(9,'wind','0005_auto_20150109_0726','2015-01-15 10:08:29.861638');
INSERT INTO "django_migrations" VALUES(10,'wind','0006_auto_20150109_0818','2015-01-15 10:08:30.354683');
INSERT INTO "django_migrations" VALUES(11,'wind','0002_auto_20150309_0727','2015-03-09 07:27:17.293290');
INSERT INTO "django_migrations" VALUES(12,'wind','0003_auto_20150310_1205','2015-03-10 12:05:43.527985');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type" VALUES(1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(3,'group','auth','group');
INSERT INTO "django_content_type" VALUES(4,'user','auth','user');
INSERT INTO "django_content_type" VALUES(5,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(7,'user profile','wind','userprofile');
INSERT INTO "django_content_type" VALUES(8,'location','wind','location');
INSERT INTO "django_content_type" VALUES(9,'factory','wind','factory');
INSERT INTO "django_content_type" VALUES(10,'power station','wind','powerstation');
INSERT INTO "django_content_type" VALUES(11,'wind turbine','wind','windturbine');
INSERT INTO "django_content_type" VALUES(12,'power data','wind','powerdata');
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
INSERT INTO "auth_permission" VALUES(1,'Can add log entry',1,'add_logentry');
INSERT INTO "auth_permission" VALUES(2,'Can change log entry',1,'change_logentry');
INSERT INTO "auth_permission" VALUES(3,'Can delete log entry',1,'delete_logentry');
INSERT INTO "auth_permission" VALUES(4,'Can add permission',2,'add_permission');
INSERT INTO "auth_permission" VALUES(5,'Can change permission',2,'change_permission');
INSERT INTO "auth_permission" VALUES(6,'Can delete permission',2,'delete_permission');
INSERT INTO "auth_permission" VALUES(7,'Can add group',3,'add_group');
INSERT INTO "auth_permission" VALUES(8,'Can change group',3,'change_group');
INSERT INTO "auth_permission" VALUES(9,'Can delete group',3,'delete_group');
INSERT INTO "auth_permission" VALUES(10,'Can add user',4,'add_user');
INSERT INTO "auth_permission" VALUES(11,'Can change user',4,'change_user');
INSERT INTO "auth_permission" VALUES(12,'Can delete user',4,'delete_user');
INSERT INTO "auth_permission" VALUES(13,'Can add content type',5,'add_contenttype');
INSERT INTO "auth_permission" VALUES(14,'Can change content type',5,'change_contenttype');
INSERT INTO "auth_permission" VALUES(15,'Can delete content type',5,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(16,'Can add session',6,'add_session');
INSERT INTO "auth_permission" VALUES(17,'Can change session',6,'change_session');
INSERT INTO "auth_permission" VALUES(18,'Can delete session',6,'delete_session');
INSERT INTO "auth_permission" VALUES(19,'Can add user profile',7,'add_userprofile');
INSERT INTO "auth_permission" VALUES(20,'Can change user profile',7,'change_userprofile');
INSERT INTO "auth_permission" VALUES(21,'Can delete user profile',7,'delete_userprofile');
INSERT INTO "auth_permission" VALUES(22,'Can add location',8,'add_location');
INSERT INTO "auth_permission" VALUES(23,'Can change location',8,'change_location');
INSERT INTO "auth_permission" VALUES(24,'Can delete location',8,'delete_location');
INSERT INTO "auth_permission" VALUES(25,'Can add factory',9,'add_factory');
INSERT INTO "auth_permission" VALUES(26,'Can change factory',9,'change_factory');
INSERT INTO "auth_permission" VALUES(27,'Can delete factory',9,'delete_factory');
INSERT INTO "auth_permission" VALUES(28,'Can add power station',10,'add_powerstation');
INSERT INTO "auth_permission" VALUES(29,'Can change power station',10,'change_powerstation');
INSERT INTO "auth_permission" VALUES(30,'Can delete power station',10,'delete_powerstation');
INSERT INTO "auth_permission" VALUES(31,'Can add wind turbine',11,'add_windturbine');
INSERT INTO "auth_permission" VALUES(32,'Can change wind turbine',11,'change_windturbine');
INSERT INTO "auth_permission" VALUES(33,'Can delete wind turbine',11,'delete_windturbine');
INSERT INTO "auth_permission" VALUES(34,'Can add power data',12,'add_powerdata');
INSERT INTO "auth_permission" VALUES(35,'Can change power data',12,'change_powerdata');
INSERT INTO "auth_permission" VALUES(36,'Can delete power data',12,'delete_powerdata');
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$12000$nEWR8stVhcNr$Z9MXLVApvomQhJ4UtIzpAY/lQALQRday8XMBmzC+2bk=','2015-03-10 11:25:00.569782',1,'super','','','super@s.com',1,1,'2015-03-10 09:26:02.951934');
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$12000$44P2DReFC4vw$+HGMxaixwsgYelO8eNDh6RVmBOMpKxp24VAAcJ3bF1Q=','2015-03-09 07:36:31',0,'system_user','','','',1,1,'2015-03-09 07:36:31');
INSERT INTO "auth_user" VALUES(3,'pbkdf2_sha256$12000$1WvC9xm1CaYJ$ENG7jcFvIXFWFSEYbjkrkXSdaUGUyNfXNQVCvwSCy1Q=','2015-03-09 07:49:59.018520',0,'factory_admin','','','',1,1,'2015-03-09 07:47:55');
INSERT INTO "auth_user" VALUES(4,'pbkdf2_sha256$12000$kTFCtG6bPG0X$3JjD05FZe4nEn9H0FFudaTI7vVbjTsMzk4BVZQsd8FE=','2015-03-09 07:50:59',0,'user1','','','',0,1,'2015-03-09 07:50:59');
INSERT INTO "auth_user" VALUES(5,'pbkdf2_sha256$12000$9ssTVixCr3dm$OYm9DCASuQApL9BcG3RiAShzsdacoU4i6ceUFheb8Cg=','2015-03-09 07:56:53.980707',0,'user2','','','',0,1,'2015-03-09 07:56:53.980765');
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
INSERT INTO "auth_user_user_permissions" VALUES(7,2,32);
INSERT INTO "auth_user_user_permissions" VALUES(8,2,35);
INSERT INTO "auth_user_user_permissions" VALUES(9,2,20);
INSERT INTO "auth_user_user_permissions" VALUES(10,2,23);
INSERT INTO "auth_user_user_permissions" VALUES(11,2,26);
INSERT INTO "auth_user_user_permissions" VALUES(12,2,29);
INSERT INTO "auth_user_user_permissions" VALUES(13,3,32);
INSERT INTO "auth_user_user_permissions" VALUES(14,3,33);
INSERT INTO "auth_user_user_permissions" VALUES(15,3,34);
INSERT INTO "auth_user_user_permissions" VALUES(16,3,35);
INSERT INTO "auth_user_user_permissions" VALUES(17,3,36);
INSERT INTO "auth_user_user_permissions" VALUES(18,3,10);
INSERT INTO "auth_user_user_permissions" VALUES(19,3,11);
INSERT INTO "auth_user_user_permissions" VALUES(20,3,12);
INSERT INTO "auth_user_user_permissions" VALUES(21,3,19);
INSERT INTO "auth_user_user_permissions" VALUES(22,3,20);
INSERT INTO "auth_user_user_permissions" VALUES(23,3,21);
INSERT INTO "auth_user_user_permissions" VALUES(24,3,22);
INSERT INTO "auth_user_user_permissions" VALUES(25,3,23);
INSERT INTO "auth_user_user_permissions" VALUES(26,3,24);
INSERT INTO "auth_user_user_permissions" VALUES(27,3,25);
INSERT INTO "auth_user_user_permissions" VALUES(28,3,26);
INSERT INTO "auth_user_user_permissions" VALUES(29,3,27);
INSERT INTO "auth_user_user_permissions" VALUES(30,3,28);
INSERT INTO "auth_user_user_permissions" VALUES(31,3,29);
INSERT INTO "auth_user_user_permissions" VALUES(32,3,30);
INSERT INTO "auth_user_user_permissions" VALUES(33,3,31);
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "django_admin_log" VALUES(1,'2015-03-09 07:36:31.798930','2','system_user',1,'',4,1);
INSERT INTO "django_admin_log" VALUES(2,'2015-03-09 07:45:51.475088','2','system_user',2,'Changed is_staff and user_permissions.',4,1);
INSERT INTO "django_admin_log" VALUES(3,'2015-03-09 07:46:34.319723','1','super',2,'Added user profile "super".',4,1);
INSERT INTO "django_admin_log" VALUES(4,'2015-03-09 07:46:42.014568','2','system_user',2,'Changed father for user profile "system_user".',4,1);
INSERT INTO "django_admin_log" VALUES(5,'2015-03-09 07:47:56.041789','3','factory_admin',1,'',4,1);
INSERT INTO "django_admin_log" VALUES(6,'2015-03-09 07:49:06.408375','3','factory_admin',2,'Changed is_staff and user_permissions.',4,1);
INSERT INTO "django_admin_log" VALUES(7,'2015-03-09 07:50:59.359453','4','user1',1,'',4,3);
INSERT INTO "django_admin_log" VALUES(8,'2015-03-09 07:51:33.894358','4','user1',2,'No fields changed.',4,3);
INSERT INTO "django_admin_log" VALUES(9,'2015-03-09 07:56:54.089707','5','user2',1,'',4,3);
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('qh1qm39rgzxon1r0jymvnugay5jo1b3g','MGQ2OTE0ZjA2OTRiZmQ1N2M1NGRjODNkMGEyZTNmNzljY2U2OTM4MTp7fQ==','2015-03-24 09:26:14.380144');
INSERT INTO "django_session" VALUES('sqv1re3v50heyu0trefjg8h3ht1iv498','ZGNkODc1MzA4ODI0YWI2NjRlNmQxYzY3ZTY5YzU0MDgxMzFlNDgxNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA5ZDk3YzMxNGIyMjhhMWM5Mzk4NGI3OTVjZmQzNTU2MDQ0YTZhZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-03-24 09:26:52.618857');
INSERT INTO "django_session" VALUES('tujvay58j609sj10alobx9fo901lcbq7','ZGNkODc1MzA4ODI0YWI2NjRlNmQxYzY3ZTY5YzU0MDgxMzFlNDgxNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA5ZDk3YzMxNGIyMjhhMWM5Mzk4NGI3OTVjZmQzNTU2MDQ0YTZhZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-03-24 11:25:00.645535');
INSERT INTO "django_session" VALUES('82x1d8s20sicoekeea0vnoupzcchlixi','MGQ2OTE0ZjA2OTRiZmQ1N2M1NGRjODNkMGEyZTNmNzljY2U2OTM4MTp7fQ==','2015-01-29 10:08:38.789123');
INSERT INTO "django_session" VALUES('gvkg0ma2rik1q4mzqxlca9bguvd29or2','MGQ2OTE0ZjA2OTRiZmQ1N2M1NGRjODNkMGEyZTNmNzljY2U2OTM4MTp7fQ==','2015-01-29 10:09:17.136654');
INSERT INTO "django_session" VALUES('ja4e1bq28jjfc7r78u26r1t4d1fkgoya','MGQ2OTE0ZjA2OTRiZmQ1N2M1NGRjODNkMGEyZTNmNzljY2U2OTM4MTp7fQ==','2015-01-29 11:33:44.222701');
INSERT INTO "django_session" VALUES('lhn1j2mbqym6b3mpp8huwwqpun9q77ba','OThjMzNkYzY3MjIzYjMyYTI4MmVlNGM1NmZjYWNhNGY4NDFjMDJkMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjJmNzM4MmMxNGRjZjAwNzcyMGNiYzdhMDU4MzhiZDhjNzQ3OTExOTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-03-23 08:00:11.984246');
INSERT INTO "django_session" VALUES('v1iaorxj5y910h6cddyu4yclq4asoqnq','OThjMzNkYzY3MjIzYjMyYTI4MmVlNGM1NmZjYWNhNGY4NDFjMDJkMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjJmNzM4MmMxNGRjZjAwNzcyMGNiYzdhMDU4MzhiZDhjNzQ3OTExOTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-03-24 10:37:55.335468');
CREATE TABLE "wind_location" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "province" varchar(30) NOT NULL, "city" varchar(30) NOT NULL, "country" varchar(30) NOT NULL);
CREATE TABLE "wind_powerstation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL, "province" varchar(50) NOT NULL, "country" varchar(50) NOT NULL, "city" varchar(50) NOT NULL, "contact" varchar(30) NOT NULL, "telephone" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "bank_account" varchar(30) NOT NULL, "begintime" datetime NULL, "endtime" datetime NULL, "factory_id" integer NOT NULL REFERENCES "wind_factory" ("id"), "location_id" integer NULL UNIQUE REFERENCES "wind_location" ("id"), "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"));
CREATE TABLE "wind_windturbine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL, "longitude" varchar(12) NOT NULL, "latitude" varchar(12) NOT NULL, "contact" varchar(30) NOT NULL, "telephone" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "begintime" datetime NULL, "endtime" datetime NULL, "location_id" integer NULL UNIQUE REFERENCES "wind_location" ("id"), "powerstation_id" integer NOT NULL REFERENCES "wind_powerstation" ("id"), "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"));
CREATE TABLE "wind_factory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL, "province" varchar(50) NOT NULL, "state" varchar(50) NOT NULL, "country" varchar(50) NOT NULL, "city" varchar(50) NOT NULL, "contact" varchar(30) NOT NULL, "telephone" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "bank_account" varchar(30) NOT NULL, "begintime" datetime NULL, "endtime" datetime NULL, "location_id" integer NULL UNIQUE REFERENCES "wind_location" ("id"), "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"));
CREATE TABLE "wind_userprofile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "address" varchar(50) NULL, "level" varchar(10) NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"), "father_id" integer NULL REFERENCES "wind_userprofile" ("id"), "telephone" varchar(30) NULL);
INSERT INTO "wind_userprofile" VALUES(1,'www@w.com','1',2,2,'10086');
INSERT INTO "wind_userprofile" VALUES(2,'cq@q.com','0',1,NULL,'10086');
INSERT INTO "wind_userprofile" VALUES(3,'q@q.com','2',3,2,'10086');
INSERT INTO "wind_userprofile" VALUES(4,'q@q.com','3',4,3,'10086');
INSERT INTO "wind_userprofile" VALUES(5,'q@q.com','3',5,3,'10086');
CREATE TABLE "wind_powerdata" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "time" varchar(30) NULL, "NWP_speed" varchar(30) NULL, "CFD_speed" varchar(30) NULL, "Observed_speed" varchar(30) NULL, "Observed_power" varchar(30) NULL, "Predicted_speed" varchar(30) NULL, "Speed_dev" varchar(30) NULL, "Predicted_power" varchar(30) NULL, "Power_dev" varchar(30) NULL, "turbine_id" integer NULL UNIQUE REFERENCES "wind_windturbine" ("id"));
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('django_content_type',12);
INSERT INTO "sqlite_sequence" VALUES('django_migrations',12);
INSERT INTO "sqlite_sequence" VALUES('wind_userprofile',5);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',36);
INSERT INTO "sqlite_sequence" VALUES('auth_user',5);
INSERT INTO "sqlite_sequence" VALUES('wind_factory',0);
INSERT INTO "sqlite_sequence" VALUES('wind_powerstation',0);
INSERT INTO "sqlite_sequence" VALUES('wind_windturbine',0);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',9);
INSERT INTO "sqlite_sequence" VALUES('auth_user_user_permissions',33);
INSERT INTO "sqlite_sequence" VALUES('wind_powerdata',0);
CREATE INDEX auth_permission_417f1b1c ON "auth_permission" ("content_type_id");
CREATE INDEX auth_group_permissions_0e939a4f ON "auth_group_permissions" ("group_id");
CREATE INDEX auth_group_permissions_8373b171 ON "auth_group_permissions" ("permission_id");
CREATE INDEX auth_user_groups_e8701ad4 ON "auth_user_groups" ("user_id");
CREATE INDEX auth_user_groups_0e939a4f ON "auth_user_groups" ("group_id");
CREATE INDEX auth_user_user_permissions_e8701ad4 ON "auth_user_user_permissions" ("user_id");
CREATE INDEX auth_user_user_permissions_8373b171 ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX django_admin_log_417f1b1c ON "django_admin_log" ("content_type_id");
CREATE INDEX django_admin_log_e8701ad4 ON "django_admin_log" ("user_id");
CREATE INDEX django_session_de54fa62 ON "django_session" ("expire_date");
CREATE INDEX wind_powerstation_f304d0ac ON "wind_powerstation" ("factory_id");
CREATE INDEX wind_windturbine_922f3874 ON "wind_windturbine" ("powerstation_id");
CREATE INDEX wind_userprofile_4138be47 ON "wind_userprofile" ("father_id");
COMMIT;