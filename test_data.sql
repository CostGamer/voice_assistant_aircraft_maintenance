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

INSERT INTO aircraft_parts (name, description, serial_number, aircraft_id) VALUES
    ('Носовая часть фюзеляжа', 'Передняя часть фюзеляжа', 'N001', (SELECT id FROM aircrafts WHERE registration_number = 'RA-89001')),
    ('Носовая опора шасси', 'Передняя стойка шасси', 'N002', (SELECT id FROM aircrafts WHERE registration_number = 'VP-BNT')),
    ('Правый двигатель', 'Правый силовой агрегат', 'N003', (SELECT id FROM aircrafts WHERE registration_number = 'VQ-BQQ')),
    ('Правая консоль крыла', 'Правая часть крыла', 'N004', (SELECT id FROM aircrafts WHERE registration_number = 'VP-BPC')),
    ('Основная стойка шасси', 'Главная опора шасси', 'N005', (SELECT id FROM aircrafts WHERE registration_number = 'VP-BVM')),
    ('Центроплан', 'Центральная часть крыла', 'N006', (SELECT id FROM aircrafts WHERE registration_number = 'RA-89001')),
    ('Хвостовая часть', 'Задняя часть самолета', 'N007', (SELECT id FROM aircrafts WHERE registration_number = 'VP-BNT')),
    ('Левая консоль крыла', 'Левая часть крыла', 'N008', (SELECT id FROM aircrafts WHERE registration_number = 'VQ-BQQ')),
    ('Левый двигатель', 'Левый силовой агрегат', 'N009', (SELECT id FROM aircrafts WHERE registration_number = 'VP-BPC'));

INSERT INTO maintenance_steps (step_name, step_count, description, part_id, status) VALUES
    ('Осмотр приемников статического давления', 1, 'Проверка приемников давления', (SELECT id FROM aircraft_parts WHERE name = 'Носовая часть фюзеляжа'), 'in_progress'),
    ('Проверка датчиков угла атаки', 2, 'Контроль датчиков угла атаки', (SELECT id FROM aircraft_parts WHERE name = 'Носовая часть фюзеляжа'), 'in_progress'),
    ('Визуальный осмотр носового обтекателя', 3, 'Проверка обтекателя', (SELECT id FROM aircraft_parts WHERE name = 'Носовая часть фюзеляжа'), 'in_progress'),
    ('Проверка люка авионики', 4, 'Контроль люка авионики', (SELECT id FROM aircraft_parts WHERE name = 'Носовая часть фюзеляжа'), 'in_progress'),
    
    ('Визуальный осмотр возможной течи жидкостей', 1, 'Поиск утечек', (SELECT id FROM aircraft_parts WHERE name = 'Носовая опора шасси'), 'in_progress'),
    ('Осмотр колёс на износ и повреждения', 2, 'Проверка состояния шин', (SELECT id FROM aircraft_parts WHERE name = 'Носовая опора шасси'), 'in_progress'),
    ('Визуальный осмотр пневматика', 3, 'Контроль пневматика', (SELECT id FROM aircraft_parts WHERE name = 'Носовая опора шасси'), 'in_progress'),
    ('Визуальный осмотр фар', 4, 'Проверка фар', (SELECT id FROM aircraft_parts WHERE name = 'Носовая опора шасси'), 'in_progress'),
    ('Проверка крышки шасси', 5, 'Осмотр крышки стойки', (SELECT id FROM aircraft_parts WHERE name = 'Носовая опора шасси'), 'in_progress');

COMMIT;