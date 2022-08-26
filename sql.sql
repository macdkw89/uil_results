-- create table for uil_results
CREATE TABLE IF NOT EXISTS uil_results (
    id INTEGER PRIMARY KEY,
    School VARCHAR,
    City VARCHAR,
    Directors VARCHAR,
    Conference VARCHAR,
    Classification VARCHAR, 
    Year INTEGER,
    Stage_Judge_1 FLOAT,
    Stage_Judge_2 FLOAT,
    Stage_Judge_3 FLOAT,
    Stage_Final FLOAT,
    SR_Judge_1 FLOAT,
    SR_Judge_2 FLOAT,
    SR_Judge_3 FLOAT,
    SR_Final VARCHAR,
    Award VARCHAR,
    Selection_1 VARCHAR,
    Selection_2 VARCHAR,
    Selection_3 VARCHAR,
    Contest_Date VARCHAR,
    Region VARCHAR,
    cj1 VARCHAR,
    cj2 VARCHAR,
    cj3 VARCHAR,
    srj1 VARCHAR,
    srj2 VARCHAR,
    srj3 VARCHAR,
    Stage_Avg FLOAT
);

DROP TABLE uil_results;