tables = {
    "Организации": "Organizations",
    "Подразделения": "Division",
    "Компьютеры": "Computers",
    "ПО": "Software",
    "Продавцы": "Seller",
    "Адреса": "Addresses"
}

tables_queries = {
    "Organizations": """SELECT * FROM Organizations;""",
    "Division": """
        SELECT 
            DISTINCT d.id_division, d.name_organization_division, o.name_organization
        FROM 
            Division d
        JOIN 
            Organizations o ON d.name_organization = o.name_organization;
    """,
    "Computers": """
        SELECT 
            DISTINCT c.id_computer, c.inventory_number, c.computer_type, 
            c.date_start, c.date_end, c.document_number, c.document_date,
            d.name_organization_division, s.software_name, f.firm_name
        FROM 
            Computers c
        JOIN 
            Division d ON c.computer_division = d.name_organization_division
        LEFT JOIN 
            Software s ON c.software = s.software_name
        LEFT JOIN 
            Firm f ON s.firm = f.firm_name;
    """,
    "Software": """
        SELECT 
            DISTINCT s.id_software, s.software_name, s.validity_period, s.cost,
            st.type_name AS software_type, f.firm_name, se.name_seller
        FROM 
            Software s
        JOIN 
            SoftwareType st ON s.software_type = st.type_name
        LEFT JOIN 
            Firm f ON s.firm = f.firm_name
        LEFT JOIN 
            Seller se ON s.name_seller = se.name_seller;
    """,
    "Seller": """
        SELECT 
            DISTINCT se.id_seller, se.name_seller, se.telephone_number, se.site_name,
            a.house_number, a.street_name, a.street_type, a.city_name, a.city_type
        FROM 
            Seller se
        LEFT JOIN 
            Addresses a ON se.seller_address_id = a.id_address;
    """,
    "Addresses": """
        SELECT 
            DISTINCT a.id_address, a.house_number,
            st_street.type_street AS street_type,
            str.street, 
            st_city.type_city AS city_type,
            c.city
        FROM 
            Addresses a
        LEFT JOIN 
            Streets str ON a.street_name = str.street
        LEFT JOIN 
            StreetTypes st_street ON a.street_type = st_street.type_street
        LEFT JOIN 
            Cities c ON a.city_name = c.city
        LEFT JOIN 
            CityTypes st_city ON a.city_type = st_city.type_city;
    """
}


