-- users
-- {"login": "pupkin", "password": "pupkin", "name": "Пупкин Василий Фёдорович"}
-- {"login": "lupkin", "password": "lupkin", "name": "Лупкин Иван Петрович"}

BEGIN;

INSERT INTO airlines (name, registration_number) VALUES
    ('Россия', 'RA-89001'),
    ('Аэрофлот', 'SU-12345'),
    ('UTair', 'UT-56789'),
    ('S7 Airlines', 'S7-98765');

INSERT INTO users_airlines (user_id, airline_id) VALUES
    ((SELECT id FROM users WHERE login = 'pupkin'), (SELECT id FROM airlines WHERE name = 'Россия')),
    ((SELECT id FROM users WHERE login = 'pupkin'), (SELECT id FROM airlines WHERE name = 'Аэрофлот')),
    ((SELECT id FROM users WHERE login = 'lupkin'), (SELECT id FROM airlines WHERE name = 'UTair')),
    ((SELECT id FROM users WHERE login = 'lupkin'), (SELECT id FROM airlines WHERE name = 'S7 Airlines'));

INSERT INTO aircrafts (aircraft_type, registration_number, serial_number) VALUES
    ('Sukhoi Superjet 100', 'RA-89001', '95001'),
    ('Airbus A320neo', 'VP-BNT', '12345'),
    ('Boeing 737-800', 'VQ-BQQ', '56789'),
    ('Airbus A321-200', 'VP-BPC', '98765'),
    ('Boeing 737-500', 'VP-BVM', '54321');

INSERT INTO users_aircrafts (user_id, aircraft_id) VALUES
    ((SELECT id FROM users WHERE login = 'pupkin'), (SELECT id FROM aircrafts WHERE registration_number = 'RA-89001')),
    ((SELECT id FROM users WHERE login = 'pupkin'), (SELECT id FROM aircrafts WHERE registration_number = 'VP-BNT')),
    ((SELECT id FROM users WHERE login = 'lupkin'), (SELECT id FROM aircrafts WHERE registration_number = 'VQ-BQQ')),
    ((SELECT id FROM users WHERE login = 'lupkin'), (SELECT id FROM aircrafts WHERE registration_number = 'VP-BPC')),
    ((SELECT id FROM users WHERE login = 'lupkin'), (SELECT id FROM aircrafts WHERE registration_number = 'VP-BVM'));

COMMIT;