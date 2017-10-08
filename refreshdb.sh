dropdb ewas
createdb ewas
psql -qe ewas < schema.sql
psql -qe ewas < dummy.sql
