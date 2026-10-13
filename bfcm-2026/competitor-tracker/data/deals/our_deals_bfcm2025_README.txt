OUR DEALS BFCM 2025 — PARTIAL NATIVE-SOURCE EXPORT
Requested scope: US and CA, every deal running or scheduled to overlap 2025-11-01 through 2025-12-05 inclusive. Not merely deals created during that period.
Extracted: 2026-10-13. Source: DataHub's Amazon-native promotion/coupon ingestion, NOT a fresh Seller Central UI export and NOT Keepa inference.

FILES
our_deals_bfcm2025.csv: exact requested 14 columns, 3,080 child-ASIN/campaign rows. Repeated ASINs across separate deals are intentional. Each notes field preserves the native campaign ID.
our_deals_bfcm2025_coverage.csv: all 11 requested product families x both marketplaces. No-record results mean unknown, not no deals.

RECOVERED
US: 31 Best/Lightning Deal campaigns, 1,936 child rows; coupon query returned no records.
CA: 13 Best/Lightning Deal campaigns, 1,142 child rows; 1 coupon adds 2 rows.
All 44 promotion campaign pages and the coupon page were fully retrieved; all native child counts match; all 44 sums of child attributed units match the campaign totals.
Other returned products are retained: this is not restricted to the minimum named products.

CRITICAL LIMITATIONS
This is NOT a complete historical deal ledger. Prime Exclusive Discount history and suppressed-deal/child-suppression audit history are unavailable in the granted data tools. Direct Seller Central is blocked: managed US profile reports unauthorized/no associated account; imported profile redirects to sign-in; existing Chrome session cannot attach. No commercial settings were changed.
All deal_price, reference_price and committed_units fields are blank because the native feed does not expose them. Revenue / units is NOT a scheduled deal price and was not used as one. Coupon discount is not the final deal price; its C$2 value is preserved only in notes.
Coupon units_sold is blank: 112 campaign redemptions cannot be assigned to either child ASIN or equated to units. The campaign's 304 clips, 112 redemptions and sales are whole-campaign metrics, not date-window or child allocations.
No source records matched Sleephoria Bamboo Sheets 6 Piece, Sleephoria Cooling Sheets 4 Piece, or Sleephoria Cooling Comforter in either marketplace. Other CA families are also unknown; see coverage CSV. This does not establish absence of deals.
No row was invented for a product or deal type with no native campaign record.

IDENTITY
Product names are normalized using exact child-ASIN -> product_id -> current product catalogue when unambiguous; otherwise native historical campaign names remain. Historical Sleep Sanctuary names are retained in notes even when the current catalogue maps them to Sleephoria.
Parent ASINs are marketplace-specific CURRENT listing enrichment as of 2026-10-13, NOT verified 2025 family membership. Global catalogue parents were NOT substituted for missing Canadian parents. Historical parent validation remains outstanding; 553 rows have blank parents.
SKU is filled only where exactly one seller SKU was returned for that marketplace/child. It is a current mapping, NOT proof that SKU participated historically. With multiple or missing mappings, SKU stays blank and candidates are in notes (484 rows). No duplicate sales were created by expanding multiple SKU candidates.

DATES AND STATUS
ISO timestamps retain the source UTC zone (Z), not US/CA local date-only values. Source query uses inclusive date-window overlap, with full campaign boundaries preserved. The CA coupon starts October 22 and is included because it overlaps November 1-16.
units_sold is Amazon's child-level attribution for the WHOLE campaign, not clipped to Nov 1-Dec 5 and not total store sales.
status=ran: native APPROVED campaign with recorded campaign activity, or coupon with redemptions. This is a campaign-level classification and does NOT prove each included child ran without suppression.
status=cancelled: native CANCELED. One US Lightning Deal (26873d31, Hanging Closet Organizer) has 214 attributed units despite CANCELED status. Both facts are preserved; do not interpret it as never having run.
An APPROVED campaign may have been pulled early while retaining APPROVED. The feed does not prove uninterrupted execution; no suppression status was invented.

SOURCE FRESHNESS
US/CA promotions: latest snapshot 2026-10-13; earliest history 2025-08-07 US / 2025-08-08 CA.
US coupons: latest snapshot 2026-10-13, history from 2024-08-19.
CA coupons: latest snapshot 2026-08-06 (stale), history from 2024-08-19. Historic records can be used as evidence, but completeness and final status are not certified.
The internal deal planning calendar returned no overlapping records, including explicit expired and rejected queries. It cannot fill the gaps.

TO COMPLETE
An authorized Seller Central US/CA session or native deal-product/PED/coupon exports with original prices, commitments, SKU membership and suppression history is required. Then reconcile by marketplace + campaign ID + child ASIN and verify historical parents/SKUs. No passwords or verification codes should be shared in chat.
