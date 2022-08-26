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

DROP TABLE IF EXISTS uil_results;
DROP TABLE IF EXISTS cj1_unique;
DROP TABLE IF EXISTS cj2_unique;
DROP TABLE IF EXISTS cj3_unique;
DROP TABLE IF EXISTS srj1_unique;
DROP TABLE IF EXISTS srj2_unique;
DROP TABLE IF EXISTS srj3_unique;
DROP TABLE IF EXISTS unique_judges;
DROP TABLE IF EXISTS unique_judges_alpha;
DROP TABLE IF EXISTS test_judges;
DROP TABLE IF EXISTS all_judges;
DROP TABLE IF EXISTS cj1_each;
DROP TABLE IF EXISTS cj2_each;
DROP TABLE IF EXISTS cj3_each;
DROP TABLE IF EXISTS srj1_each;
DROP TABLE IF EXISTS srj2_each;
DROP TABLE IF EXISTS srj3_each;
DROP TABLE IF EXISTS judges_each;
DROP TABLE IF EXISTS top_judges;

SELECT cj1 into cj1_each from uil_results;
SELECT cj2 into cj2_each from uil_results;
SELECT cj3 into cj3_each from uil_results;
SELECT srj1 into srj1_each from uil_results;
SELECT srj2 into srj2_each from uil_results;
SELECT srj3 into srj3_each from uil_results;
SELECT * into judges_each from (
    select * from cj1_each union all
    select * from cj2_each union all
    select * from cj3_each union all
    select * from srj1_each union all
    select * from srj2_each union all
    select * from srj3_each 
) b;

SELECT cj1, count(*) into judge_counts from judges_each group by cj1 order by count desc;
select * into top_judges from judge_counts where (count > 400) AND length(cj1) > 3;
select * from top_judges;

SELECT DISTINCT cj1 into cj1_unique FROM uil_results ORDER BY cj1;
SELECT DISTINCT cj2 into cj2_unique FROM uil_results ORDER BY cj2;
SELECT DISTINCT cj3 into cj3_unique FROM uil_results ORDER BY cj3;
SELECT DISTINCT srj1 into srj1_unique FROM uil_results ORDER BY srj1;
SELECT DISTINCT srj2 into srj2_unique FROM uil_results ORDER BY srj2;
SELECT DISTINCT srj3 into srj3_unique FROM uil_results ORDER BY srj3;

SELECT COUNT(*) FROM cj1_unique;
SELECT COUNT(*) FROM cj2_unique;
SELECT COUNT(*) FROM cj3_unique;
SELECT COUNT(*) FROM srj1_unique;
SELECT COUNT(*) FROM srj2_unique;
SELECT COUNT(*) FROM srj3_unique;

SELECT * into all_judges from (
    select * from cj1_unique union
    select * from cj2_unique union
    select * from cj3_unique union
    select * from srj1_unique union
    select * from srj2_unique union
    select * from srj3_unique 
) a;

SELECT DISTINCT * into unique_judges from all_judges;

ALTER TABLE unique_judges RENAME COLUMN cj1 to unique_judges;

SELECT * into unique_judges_alpha from unique_judges order by unique_judges;

select * from unique_judges_alpha where unique_judges like '%, %';

select * into test_judges from unique_judges_alpha;

select * from test_judges;

SELECT cj1 from judges_each;


























