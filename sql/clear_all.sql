-- Clear all tables in FK-safe order (children before parents)
DELETE FROM stars;
DELETE FROM reviews;
DELETE FROM features;
DELETE FROM products;
DELETE FROM places;
DELETE FROM reviewers;
DELETE FROM categories;
