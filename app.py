import streamlit as st

# inputs
average_concurrent_metrics = st.number_input('average concurrent metrics', value=2500)

# maximum_disk_size_mb
c1r1, c2r1, c3r1 = st.columns(3)
maximum_disk_size_mb_tier_0 = c1r1.number_input('maximum disk size (MB) - Tier 0', value=1024)
maximum_disk_size_mb_tier_1 = c2r1.number_input('maximum disk size (MB) - Tier 1', value=384)
maximum_disk_size_mb_tier_2 = c3r1.number_input('maximum disk size (MB) - Tier 2', value=192)

# update_every_sec
c1r2, c2r2, c3r2 = st.columns(3)
update_every_sec_tier_0 = c1r2.number_input('update every (sec) - Tier 0', value=1)
update_every_sec_tier_1 = c2r2.number_input('update every (sec) - Tier 1', value=60)
update_every_sec_tier_2 = c3r2.number_input('update every (sec) - Tier 2', value=3600)

# page_cache_size_mb
c1r3, c2r3, c3r3 = st.columns(3)
page_cache_size_mb_tier_0 = c1r3.number_input('page cache size (MB)  - Tier 0', value=64)
page_cache_size_mb_tier_1 = c2r3.number_input('page cache size (MB)  - Tier 1', value=36)
page_cache_size_mb_tier_2 = c3r3.number_input('page cache size (MB)  - Tier 2', value=36)

# dump inputs to screen
st.write('average_concurrent_metrics = ', average_concurrent_metrics)
st.write('maximum_disk_size_mb_tier_0 = ', maximum_disk_size_mb_tier_0)
st.write('maximum_disk_size_mb_tier_1 = ', maximum_disk_size_mb_tier_1)
st.write('maximum_disk_size_mb_tier_2 = ', maximum_disk_size_mb_tier_2)
st.write('update_every_sec_tier_0 = ', update_every_sec_tier_0)
st.write('update_every_sec_tier_1 = ', update_every_sec_tier_1)
st.write('update_every_sec_tier_2 = ', update_every_sec_tier_2)
st.write('page_cache_size_mb_tier_0 = ', page_cache_size_mb_tier_0)
st.write('page_cache_size_mb_tier_1 = ', page_cache_size_mb_tier_1)
st.write('page_cache_size_mb_tier_2 = ', page_cache_size_mb_tier_2)