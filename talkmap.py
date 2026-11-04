# Leaflet cluster map of talk locations
#
# Run this from the repository root (or any working directory). It reads
# Markdown files in `_talks/`, geolocates the location YAML field with
# geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# talkmap Jupyter notebook.
import os
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files from this repository, not the process working directory.
ROOT = os.path.dirname(os.path.abspath(__file__))
g = glob.glob(os.path.join(ROOT, "_talks", "*.md"))

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    location = str(data.get('location') or '').strip()
    if not location:
        continue

    # Prepare the description
    title = str(data.get('title') or '').strip()
    venue = str(data.get('venue') or '').strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location and report the status. A miss returns None rather than raising.
    try:
        geocoded = geocoder.geocode(location, timeout=TIMEOUT)
        if geocoded is None:
            print(f"Error: no geocode result for {location}")
            continue
        location_dict[description] = geocoded
        print(description, geocoded)
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {location} with message {ex}")

# Save the map next to this script. Skip output when every lookup failed so a
# partial geocoder outage does not replace a previously good map with an empty one.
if location_dict:
    os.chdir(ROOT)
    getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
else:
    print("No talk locations were geocoded; left the existing map in place.")
