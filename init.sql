create table weights (
    scenario varchar(9) not null,
    position tinyint not null,
    weight float,
    primary key (scenario, position)
);

create table games (
    gameid varchar(36) primary key,
    outcome boolean
);

create table moves (
    moveid int not null,
    gameid varchar(36) not null,
    isHuman boolean not null,
    position tinyint not null,
    primary key (moveid, gameid),
    foreign key (gameid) references games(gameid)
);