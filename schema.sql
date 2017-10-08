drop table if exists agents;
create table agents (
	id serial primary key,
	name text not null,
	lat text,
	lon text,
	status text not null default 'created',

	UNIQUE(name)
);

drop table if exists sensors;
create table sensors (
	id serial primary key,
	label text not null,
	lat text not null,
	lon text not null,
	status text not null default 'created',
	threshold integer not null,
	flag boolean,

	UNIQUE(label)
);

drop table if exists jobs;
create table jobs (
	id serial primary key,
	dt_init timestamp without time zone not null default CURRENT_TIMESTAMP,
	status text not null default 'created',
	dt_finish timestamp without time zone,
	sensor_id integer references sensors(id),
	agent_id integer references agents(id)
);

drop table if exists sensor_data;
create table sensor_data (
	id serial primary key,
	flow integer not null,
	dt timestamp without time zone not null default CURRENT_TIMESTAMP,
	sensor_id integer references sensors(id)
);
