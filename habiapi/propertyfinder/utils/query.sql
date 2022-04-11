SELECT
    property.address as address, property.city as city,
    status.name as status, property.price as price,
    property.description as description
FROM property
INNER JOIN status_history
    ON property.id=status_history.property_id
INNER JOIN status
    ON status_history.status_id=status.id
WHERE status.name IN ("pre_venta", "en_venta", "vendido")