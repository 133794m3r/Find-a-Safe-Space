--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-4)
-- Dumped by pg_dump version 12.2 (Debian 12.2-4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: connect_together; Type: DATABASE; Schema: -; Owner: root
--

CREATE DATABASE connect_together WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE connect_together OWNER TO root;

\connect connect_together

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: connect_together; Type: DATABASE PROPERTIES; Schema: -; Owner: root
--

ALTER DATABASE connect_together SET search_path TO 'public', 'connect_together';


\connect connect_together

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: connect_together; Type: SCHEMA; Schema: -; Owner: root
--

CREATE SCHEMA connect_together;


ALTER SCHEMA connect_together OWNER TO root;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: event_schedules; Type: TABLE; Schema: connect_together; Owner: root
--

CREATE TABLE connect_together.event_schedules (
    id bigint NOT NULL,
    uid character(28) DEFAULT ''::bpchar NOT NULL,
    start_time numeric DEFAULT '0'::numeric NOT NULL,
    password character varying(255) DEFAULT NULL::character varying,
    edit_pass character(28) NOT NULL,
    event_location character varying(100) DEFAULT ''::character varying NOT NULL,
    event_description character varying(100) DEFAULT ''::character varying NOT NULL,
    title character varying(255) DEFAULT NULL::character varying,
    yes smallint DEFAULT 0,
    no smallint DEFAULT 0,
    maybe smallint DEFAULT 0,
    host_name character varying(255)
);


ALTER TABLE connect_together.event_schedules OWNER TO root;

--
-- Name: event_schedules_id_seq; Type: SEQUENCE; Schema: connect_together; Owner: root
--

CREATE SEQUENCE connect_together.event_schedules_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE connect_together.event_schedules_id_seq OWNER TO root;

--
-- Name: event_schedules_id_seq; Type: SEQUENCE OWNED BY; Schema: connect_together; Owner: root
--

ALTER SEQUENCE connect_together.event_schedules_id_seq OWNED BY connect_together.event_schedules.id;


--
-- Name: user_reservations; Type: TABLE; Schema: connect_together; Owner: root
--

CREATE TABLE connect_together.user_reservations (
    id bigint NOT NULL,
    reservation_uid character(28) NOT NULL,
    choice smallint NOT NULL,
    event_id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE connect_together.user_reservations OWNER TO root;

--
-- Name: user_reservations_id_seq; Type: SEQUENCE; Schema: connect_together; Owner: root
--

CREATE SEQUENCE connect_together.user_reservations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE connect_together.user_reservations_id_seq OWNER TO root;

--
-- Name: user_reservations_id_seq; Type: SEQUENCE OWNED BY; Schema: connect_together; Owner: root
--

ALTER SEQUENCE connect_together.user_reservations_id_seq OWNED BY connect_together.user_reservations.id;


--
-- Name: event_schedules id; Type: DEFAULT; Schema: connect_together; Owner: root
--

ALTER TABLE ONLY connect_together.event_schedules ALTER COLUMN id SET DEFAULT nextval('connect_together.event_schedules_id_seq'::regclass);


--
-- Name: user_reservations id; Type: DEFAULT; Schema: connect_together; Owner: root
--

ALTER TABLE ONLY connect_together.user_reservations ALTER COLUMN id SET DEFAULT nextval('connect_together.user_reservations_id_seq'::regclass);


--
-- Data for Name: event_schedules; Type: TABLE DATA; Schema: connect_together; Owner: root
--

INSERT INTO connect_together.event_schedules (id, uid, start_time, password, edit_pass, event_location, event_description, title, yes, no, maybe, host_name) VALUES (2, '0l9kea3b6PC35P6wooh2eWRdsKA=', 1594430100.0, '', 'KODU_RJMUqOfCVgyoPB05lm5yRY=', 'the park', 'We''re going to meetup somewhere together.', 'test', 2, 1, 3, 'Joanne');
INSERT INTO connect_together.event_schedules (id, uid, start_time, password, edit_pass, event_location, event_description, title, yes, no, maybe, host_name) VALUES (3, 'ypEHo9xtTindNJHq2VEl2sZ15p0=', 1594624500.0, 'secret', '-ZBBLvFR7i2RybC8uvYiyDvAy-4=', 'Macarthur''s House', 'We will have a Pizza Party through Zoom.', 'Pizza Party Meetup', 2, 0, 0, 'Macarthur Inbody');
INSERT INTO connect_together.event_schedules (id, uid, start_time, password, edit_pass, event_location, event_description, title, yes, no, maybe, host_name) VALUES (4, '6KXcQkFRAbqt-EB3_gjgtPrMYNM=', 1595589300.0, '', '6HDrvl4oGBK2DJ-y7GxrrfTEhds=', 'Macarthur''s House', 'We will have a Pizza Party through Zoom.', 'Pizza Party Meetup', 1, 1, 0, 'Macarthur Inbody');


--
-- Data for Name: user_reservations; Type: TABLE DATA; Schema: connect_together; Owner: root
--

INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (3, 'FXdst9seZrzFssCKgVEUYptfIww=', 1, 2, 'jimmy jon');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (5, 'I1B4AaGO3p_LGUnRcEXrBIV17Sc=', 1, 2, 'jon jon');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (6, '-OBvGr4h97UxLmfEkKZg9SIxF88=', 3, 2, 'bobby');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (7, 'WR1mpEPJEWVlA4CKBGN0ML1dmKA=', 3, 2, 'jimmy');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (8, 'QYtqT8yY11po-HCw2miHLu8rfrA=', 3, 2, 'timmy');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (9, '3jT7EVp5f_OJqMnq2NMvqHo7Lg8=', 2, 2, 'who');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (11, 'XMKfS5jhTVmzMnkYN-26EKnlIsQ=', 1, 3, 'David Inbody');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (12, 'Kbjfpto_E0Z6T6Wfpj44xb6TWYU=', 1, 3, 'Macarthur Inbody');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (13, '2xOaivOk1KXxXSU-IRUwyfrEBZk=', 1, 4, 'Macarthur Inbody');
INSERT INTO connect_together.user_reservations (id, reservation_uid, choice, event_id, name) VALUES (14, 'Z84fTeTnEAF-zrkux0tqJOeC2Ms=', 2, 4, 'David Inbody');


--
-- Name: event_schedules_id_seq; Type: SEQUENCE SET; Schema: connect_together; Owner: root
--

SELECT pg_catalog.setval('connect_together.event_schedules_id_seq', 4, true);


--
-- Name: user_reservations_id_seq; Type: SEQUENCE SET; Schema: connect_together; Owner: root
--

SELECT pg_catalog.setval('connect_together.user_reservations_id_seq', 14, true);


--
-- Name: event_schedules idx_41051_primary; Type: CONSTRAINT; Schema: connect_together; Owner: root
--

ALTER TABLE ONLY connect_together.event_schedules
    ADD CONSTRAINT idx_41051_primary PRIMARY KEY (id);


--
-- Name: user_reservations idx_41066_primary; Type: CONSTRAINT; Schema: connect_together; Owner: root
--

ALTER TABLE ONLY connect_together.user_reservations
    ADD CONSTRAINT idx_41066_primary PRIMARY KEY (id);


--
-- Name: idx_41051_event_schedules_uid_k; Type: INDEX; Schema: connect_together; Owner: root
--

CREATE UNIQUE INDEX idx_41051_event_schedules_uid_k ON connect_together.event_schedules USING btree (uid);


--
-- PostgreSQL database dump complete
--

