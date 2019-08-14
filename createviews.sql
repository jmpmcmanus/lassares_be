CREATE VIEW lassares_be_app_testdatav_model AS SELECT fid AS id, device_id, timestamp, job_id, chem_id FROM lassares_be_app_testdata_model;
CREATE VIEW lassares_be_app_timestamp_model AS SELECT timestamp as id, timestamp as label FROM lassares_be_app_testdata_model;
CREATE VIEW lassares_be_app_jobid_model AS SELECT DISTINCT job_id as id, job_id as label FROM lassares_be_app_testdata_model;
