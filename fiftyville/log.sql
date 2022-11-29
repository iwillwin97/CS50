-- Keep a log of any SQL queries you execute as you solve the mystery.
--First step is to get a report description from crime reports to look for some more clues
SELECT description FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND year = 2021
AND street = 'Humphrey Street';

--As the report mentions about three witness looking at their interview transcripts would be helful.
SELECT name, transcript
FROM interviews
WHERE day = 28
AND month = 7
AND year = 2021;