-- Enforce one review per reviewer per product per place
ALTER TABLE reviews
  ADD CONSTRAINT reviews_unique_reviewer_place_product
  UNIQUE (reviewer_id, place_id, product_id);
