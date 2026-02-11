-- Assumes that we are in the ruta database

CREATE TABLE establishment (
  id BIGSERIAL PRIMARY KEY,
  place GEOMETRY,
  osm_type TEXT,
  osm_id BIGINT,
  tags JSONB
);

\copy establishment(place, osm_type, osm_id, tags) FROM './data/madrid-ruta.pg';
