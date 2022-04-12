SELECT
    property.address as address, property.city as city,
    status.name as status, property.price as price,
    property.description as description
FROM property
INNER JOIN (
    SELECT property_id, status_id, MAX(update_date) max_date
    FROM status_history
    GROUP BY property_id
) recent_status ON property.id=recent_status.property_id
INNER JOIN status_history
    ON property.id=status_history.property_id
INNER JOIN status
    ON recent_status.status_id=status.id
WHERE status.name IN ("pre_venta", "en_venta", "vendido") AND property.city="medellin"