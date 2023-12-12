CREATE TABLE Organizations (
    id_organization uuid not null PRIMARY KEY,
    name_organization VARCHAR(255) NOT NULL UNIQUE,
	shortname_organization varchar(128) default null
);

CREATE TABLE Division (
    id_division uuid not null PRIMARY KEY,
    name_organization VARCHAR(255),
    name_organization_division VARCHAR(255) UNIQUE,
    FOREIGN KEY (name_organization) references Organizations (name_organization) on delete set null
);

CREATE TABLE Firm (
    id_firm uuid not null PRIMARY KEY,
    firm_name VARCHAR(255) not null UNIQUE
);

CREATE TABLE SoftwareType (
    id_type uuid not null PRIMARY KEY,
    type_name VARCHAR(255) not null UNIQUE
);


CREATE TABLE StreetTypes (
    id_type uuid not null PRIMARY KEY,
    type_street VARCHAR(255) UNIQUE
);

CREATE TABLE Streets (
    id_street uuid not null PRIMARY KEY,
    street VARCHAR(255) UNIQUE,
    street_type VARCHAR(255),
    FOREIGN KEY (id_street) references StreetTypes (id_type) on delete set null
);


CREATE TABLE CityTypes (
    id_type uuid not null PRIMARY KEY,
    type_city VARCHAR(255) UNIQUE
);

CREATE TABLE Cities (
    id_city uuid not null PRIMARY KEY,
    city VARCHAR(255) UNIQUE,
    city_type VARCHAR(255),
    FOREIGN KEY (city_type) references CityTypes (type_city) on delete set null
);

CREATE TABLE Addresses (
    id_address uuid not null PRIMARY KEY,
    house_number VARCHAR(255),
    street_name VARCHAR(255),
    street_type_id uuid not null,
    FOREIGN KEY (street_name) references Streets (street) on delete set null,
    FOREIGN KEY (street_type_id) references Streets (id_street) on delete set null,
    city_name VARCHAR(255),
    city_type VARCHAR(255),
    FOREIGN KEY (city_name) references Cities (city) on delete set null,
    FOREIGN KEY (city_type) references CityTypes (type_city) on delete set null
);

CREATE TABLE Seller (
    id_seller uuid not null PRIMARY KEY,
    name_seller VARCHAR(255) not null UNIQUE,
    telephone_number VARCHAR(255) not null,
    site_name VARCHAR(255) not null,
    seller_address_id uuid not null,
    FOREIGN KEY (seller_address_id) references Addresses (id_address) on delete set null
);


CREATE TABLE Software (
    id_software uuid not null PRIMARY KEY,
    software_name VARCHAR(255) UNIQUE,
    validity_period INTERVAL,
    cost NUMERIC(10, 2) not null,
    software_type VARCHAR(255),
    FOREIGN KEY (software_type) references SoftwareType (type_name) on delete set null,
    firm VARCHAR(255),
    FOREIGN KEY (firm) references Firm (firm_name) on delete set null,
    name_seller VARCHAR(255) not null,
    FOREIGN KEY (name_seller) references Seller (name_seller) on delete set null
);



CREATE TABLE Computers (
    id_computer uuid not null PRIMARY KEY,
    inventory_number integer not null,
    computer_type VARCHAR(255) not null, -- server or station
    date_start DATE not null,
    date_end DATE not null,
    document_number integer not null,
    document_date DATE not null,
    software VARCHAR(255) ,
    computer_division VARCHAR(255),
    FOREIGN KEY (computer_division) references Division (name_organization_division) on delete set null,
    FOREIGN KEY (software) references Software (software_name) on delete set null
);