with source_listings as (
    select * from {{ source('dbt_airbnb_project', 'listings') }}
)

    select
        id,
        host_id,
        host_listings_count,
        host_total_listings_count,
        price,
        review_scores_rating,
        reviews_per_month,
        host_is_superhost,
        host_identity_verified,
        has_availability,
        instant_bookable,
        listing_url,
        name,
        description
    from source_listings
