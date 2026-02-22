-- Migration: add category_id to places (for existing Supabase databases)
-- Run this in the Supabase SQL editor if the places table already exists.

ALTER TABLE places
    ADD COLUMN category_id integer references categories (id);
