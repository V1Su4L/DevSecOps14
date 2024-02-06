CREATE TABLE colors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  hex_code VARCHAR(7)
);

INSERT INTO colors (name, hex_code)
VALUES
  ('Red', '#FF0000'),
  ('Green', '#00FF00'),
  ('Blue', '#0000FF');