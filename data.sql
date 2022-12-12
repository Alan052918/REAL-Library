-- populating the rooms_room table
INSERT INTO rooms_room (id, capacity, location) VALUES (110, 5, "Dibner 4th floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (111, 5, "Dibner 4th floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (118, 3, "Dibner 3rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (119, 3, "Dibner 3rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (112, 5, "Dibner 3rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (113, 4, "Bobst 5rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (114, 4, "Bobst 3rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (115, 4, "Bobst 3rd floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (116, 3, "Bobst 6th floor");
INSERT INTO rooms_room (id, capacity, location) VALUES (117, 3, "Bobst 6th floor");

-- populating the inventory_topic table
INSERT INTO inventory_topic (id, name, description) VALUES (1, 'Horror', 'Horror genre');
INSERT INTO inventory_topic (id, name, description) VALUES (2, 'History', 'History genre');
INSERT INTO inventory_topic (id, name, description) VALUES (3, 'Murder', 'Murder genre');
INSERT INTO inventory_topic (id, name, description) VALUES (4, 'Mystery', 'Mystery genre');
INSERT INTO inventory_topic (id, name, description) VALUES (5, 'Detective', 'Detective genre');
INSERT INTO inventory_topic (id, name, description) VALUES (6, '5G', '5G academic conference');
INSERT INTO inventory_topic (id, name, description) VALUES (7, 'ML', 'Machine learning conference');
INSERT INTO inventory_topic (id, name, description) VALUES (8, 'Science', 'Science genre');
INSERT INTO inventory_topic (id, name, description) VALUES (9, 'Arts', 'Arts genre');
INSERT INTO inventory_topic (id, name, description) VALUES (10, 'Physics', 'Physics related conference');

-- populating the events_exhibition table
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (1, 'EVENT1', 'Exhibition', DATE '2015-12-1', DATE '2015-12-2', 123.00, 3);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (3, 'EVENT3', 'Exhibition', DATE '2015-11-1', DATE '2015-11-2', 100.15, 2);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (5, 'EVENT5', 'Exhibition', DATE '2015-7-1', DATE '2015-7-2', 201.00, 1);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (7, 'EVENT7', 'Exhibition', DATE '2015-5-1', DATE '2015-5-2', 550.50, 2);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (8, 'EVENT8', 'Exhibition', DATE '2015-4-1', DATE '2015-4-2', 120.50, 3);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (9, 'EVENT9', 'Exhibition', DATE '2015-3-1', DATE '2015-3-2', 450.60, 1);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (10, 'EVENT10', 'Exhibition', DATE '2015-1-1', DATE '2015-1-2', 100.20, 3);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (11, 'EVENT11', 'Exhibition', DATE '2016-1-1', DATE '2016-1-2', 205.00, 3);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (12, 'EVENT12', 'Exhibition', DATE '2017-1-1', DATE '2017-1-2', 800.00, 2);
INSERT INTO events_exhibition (id, name, type, start_datetime, stop_datetime, expense, topic_id) VALUES (13, 'EVENT13', 'Exhibition', DATE '2018-1-1', DATE '2018-1-2', 151.60, 1);

-- populating the events_seminar table
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (2, 'EVENT2', 'Seminar', DATE '2015-12-11', DATE '2015-12-12', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (4, 'EVENT4', 'Seminar', DATE '2015-8-1', DATE '2015-8-2', 3);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (6, 'EVENT6', 'Seminar', DATE '2015-6-1', DATE '2015-6-2', 3);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (14, 'EVENT14', 'Seminar', DATE '2018-1-2', DATE '2018-1-3', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (15, 'EVENT15', 'Seminar', DATE '2018-1-4', DATE '2018-1-5', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (16, 'EVENT16', 'Seminar', DATE '2018-1-6', DATE '2018-1-7', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (17, 'EVENT17', 'Seminar', DATE '2018-1-8', DATE '2018-1-9', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (18, 'EVENT18', 'Seminar', DATE '2018-1-10', DATE '2018-1-11', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (19, 'EVENT19', 'Seminar', DATE '2018-1-12', DATE '2018-1-13', 1);
INSERT INTO events_seminar (id, name, type, start_datetime, stop_datetime, topic_id) VALUES (20, 'EVENT20', 'Seminar', DATE '2018-1-14', DATE '2018-1-15', 1);

-- populating the events_sponsor table
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (1, 'Jenny', 'Smith', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (2, 'Jenny', 'Johnson', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (3, 'Jenny', 'Gerard', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (4, 'Jenny', 'Atkinson', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (5, 'Jenny', 'Cumberbatch', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (6, 'Jenny', 'Fox', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (7, 'Jenny', 'Blunt', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (8, 'Jenny', 'Portman', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (9, 'Jenny', 'Shruti', 'Individual');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (10, 'Jenny', 'Gote', 'Individual');

INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (11, 'Google', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (12, 'Meta', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (13, 'Microsoft', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (14, 'Apple', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (15, 'Netflix', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (16, 'Amazon', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (17, 'IBM', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (18, 'Salesforce', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (19, 'Uber', NULL, 'Organization');
INSERT INTO events_sponsor (id, first_name, last_name, type) VALUES (20, 'Lyft',  NULL, 'Organization');

-- populating for events_seminarsponsor intersect table
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (1, 2352.12, 2, 14);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (2, 3352.12, 4, 2);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (3, 4352.12, 6, 4);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (4, 5352.12, 14, 6);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (5, 6352.12, 14, 15);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (6, 7352.12, 15, 16);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (7, 8352.12, 16, 17);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (8, 9352.12, 17, 18);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (9, 352.12, 18, 19);
INSERT INTO events_seminarsponsor (id, amount, seminar_id, sponsor_id) VALUES (10, 752.12, 19, 20);

-- populating for inventory_author table
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (1, 'Johnny', 'Bravo', 'johnnybravo@gmail.com', 'Street 1', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (2, 'Hillary', 'Bravo', 'hillarybravo@gmail.com', 'Street 2', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (3, 'John', 'Bravo', 'johnbravo@gmail.com', 'Street 3', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (4, 'Cece', 'Bravo', 'cecebravo@gmail.com', 'Street 4', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (5, 'Jack', 'Bravo', 'jackbravo@gmail.com', 'Street 5', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (6, 'Jill', 'Bravo', 'jillbravo@gmail.com', 'Street 6', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (7, 'Jenny', 'Bravo', 'jennybravo@gmail.com', 'Street 7', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (8, 'Johnston', 'Bravo', 'johnstonbravo@gmail.com', 'Street 8', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (9, 'Jerry', 'Bravo', 'jerrybravo@gmail.com', 'Street 9', 'Brooklyn', 'NY', 11220);
INSERT INTO inventory_author (id, first_name, last_name, email, street, city, state, zipcode) VALUES (10, 'Jerma', 'Bravo', 'jermabravo@gmail.com', 'Street 10', 'Brooklyn', 'NY', 11220);

-- populating for events_seminarauthor intersect table
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1111, 1, 2);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1112, 2, 4);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1113, 3, 6);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1114, 4, 14);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1115, 5, 15);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1116, 6, 16);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1117, 7, 17);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1118, 8, 18);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1119, 9, 19);
INSERT INTO events_seminarauthor (id, author_id, seminar_id) VALUES (1120, 10, 20);

-- populating for inventory_book table
INSERT INTO inventory_book (id, name, topic_id) VALUES (1, 'Calculs 1', 1);
INSERT INTO inventory_book (id, name, topic_id) VALUES (2, 'History Grade 1', 2);
INSERT INTO inventory_book (id, name, topic_id) VALUES (3, 'Murder Mayhem 1', 3);
INSERT INTO inventory_book (id, name, topic_id) VALUES (4, 'Hardy Boys 1', 4);
INSERT INTO inventory_book (id, name, topic_id) VALUES (5, 'Sherlock Holmes 1', 5);
INSERT INTO inventory_book (id, name, topic_id) VALUES (6, '5G commications  Part 1', 6);
INSERT INTO inventory_book (id, name, topic_id) VALUES (7, 'Intro to ML 1', 7);
INSERT INTO inventory_book (id, name, topic_id) VALUES (8, 'Science Part 1', 8);
INSERT INTO inventory_book (id, name, topic_id) VALUES (9, 'Painting Volume 1', 9);
INSERT INTO inventory_book (id, name, topic_id) VALUES (10, 'Mechanics Vol 1', 10);

-- populating the inventory_copy table
INSERT INTO inventory_copy (id, status, book_id) VALUES (1, 'Available', 1);
INSERT INTO inventory_copy (id, status, book_id) VALUES (2, 'Available', 1);
INSERT INTO inventory_copy (id, status, book_id) VALUES (3, 'Borrowed', 1);
INSERT INTO inventory_copy (id, status, book_id) VALUES (5, 'Lost', 3);
INSERT INTO inventory_copy (id, status, book_id) VALUES (20, 'Available', 2);
INSERT INTO inventory_copy (id, status, book_id) VALUES (30, 'Borrowed', 2);
INSERT INTO inventory_copy (id, status, book_id) VALUES (10, 'Available', 3);
INSERT INTO inventory_copy (id, status, book_id) VALUES (21, 'Borrowed', 3);
INSERT INTO inventory_copy (id, status, book_id) VALUES (31, 'Available', 3);
INSERT INTO inventory_copy (id, status, book_id) VALUES (41, 'Damaged', 3);

-- populating the inventory_bookauthor table
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (1, 1, 1);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (2, 2, 2);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (3, 3, 3);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (4, 4, 4);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (5, 5, 5);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (6, 6, 6);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (7, 7, 7);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (8, 8, 8);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (9, 9, 9);
INSERT INTO inventory_bookauthor (id, author_id, book_id) VALUES (10, 10, 10);

-- populating the inventory_rental table
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (1, 'Returned', DATE '2017-11-30', DATE '2017-12-10', DATE '2017-12-8', 1);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (2, 'Returned', DATE '2017-10-31', DATE '2017-11-10', DATE '2017-12-18', 2);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (3, 'Returned', DATE '2016-10-30', DATE '2016-12-10', DATE '2016-12-8', 3);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (4, 'Returned', DATE '2019-10-30', DATE '2019-12-10', DATE '2019-12-8', 20);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (5, 'Returned', DATE '2020-10-30', DATE '2020-12-10', DATE '2020-12-8', 30);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (6, 'Returned', DATE '2021-10-30', DATE '2021-12-10', DATE '2021-12-8', 10);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (7, 'Returned', DATE '2012-10-30', DATE '2012-12-10', DATE '2012-12-8', 21);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (8, 'Returned', DATE '2013-10-30', DATE '2013-12-10', DATE '2013-12-8', 31);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (9, 'Returned', DATE '2014-10-30', DATE '2014-12-10', DATE '2014-12-8', 41);
INSERT INTO inventory_rental (id, status, borrow_date, expected_return, actual_return, copy_id) VALUES (10, 'Returned', DATE '2015-10-30', DATE '2015-12-10', DATE '2015-12-8', 5);

-- populating the inventory_invoice table (note: the invoice amount was calculated by hand here. Sample values. Change later to calculate using the trigger
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (1, DATE '2017-12-8', 1.60, 1);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (2, DATE '2017-12-18', 17.20, 2);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (3, DATE '2016-12-8', 7.60, 3);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (4, DATE '2019-12-8', 17.20, 4);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (5, DATE '2020-12-8', 17.20, 5);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (6, DATE '2021-12-8', 17.20, 6);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (7, DATE '2012-12-8', 17.20, 7);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (8, DATE '2013-12-8', 17.20, 8);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (9, DATE '2014-12-8', 17.20, 9);
INSERT INTO inventory_invoice (id, date, amount, rental_id) VALUES (10, DATE '2015-12-8', 17.20, 10);

-- populating the inventory_payment table
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (1, DATE '2022-11-4', 'Credit', 'jayant', 'raj', 0.60, 1);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (2, DATE '2022-11-5', 'Credit', 'jayant', 'raj', 1.00, 1);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (3, DATE '2022-11-4', 'Credit', 'johnny', 'bravo', 1.00, 2);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (4, DATE '2022-11-5', 'Credit', 'johnny', 'bravo', 0.20, 2);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (5, DATE '2022-11-6', 'Credit', 'johnny', 'bravo', 16.00, 2);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (6, DATE '2022-11-4', 'Debit', 'johnny', 'silva', 1.00, 4);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (7, DATE '2022-11-5', 'Debit', 'johnny', 'bravo', 0.20, 4);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (8, DATE '2022-11-6', 'Credit', 'johnny', 'bravo', 16.00, 4);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (9, DATE '2022-11-2', 'PayPal', 'joanna', 'bravo', 0.20, 6);
INSERT INTO inventory_payment (id, date, method, first_name, last_name, amount, invoice_id) VALUES (10, DATE '2022-11-3', 'Cash', 'joanna', 'bravo', 16.00, 6);
