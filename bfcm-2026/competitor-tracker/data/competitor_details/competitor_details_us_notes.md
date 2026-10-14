# Competitor details US — Part A validation notes

- Scope: 257 requested US ASINs in the exact user-supplied order.
- Source: signed-out Amazon.com exact-ASIN pages delivered to ZIP 10001.
- Observation date: 2026-10-14.
- Output schema: exactly the 17 requested columns; 257 data rows; no duplicate requested ASINs.
- Exact identity: 253 pages retained the requested ASIN. Four requested ASINs redirected to a different ASIN; their destination fields were not substituted.
- Redirected requests: B0DG2HRZKK, B09G8P3X6L, B0D4PKVNWB, B0D1RBXBNG.
- Verified coverage: parent ASIN 253; main image URL 253; selected one-time purchase price 223; size 201; color 225.
- Stock evidence: 245 rows Y from Add to Cart or explicit availability; 12 blank where stock status was not established; no missing value was encoded as zero or N.
- Size and color come only from exact-page overview/catalog attributes. No title inference was used.
- Current price excludes crossed-out/list-price and conditional Subscribe & Save or card-offer amounts. List price is populated only from crossed/basis-price evidence.
- Parent ASIN is populated only where the exact page exposed one unique verified parent candidate.
- Variation count is blank for all rows because full family coverage was not established from the captured exact-child pages.
- Main image URLs are the full exact-page `data-old-hires` URLs when present; no URL transformation was invented.
- SHA-256: b265d7fcfc1aada050a7dffc609f99607a4b3cd3101882397d67678e52c24040.

