#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
#      Cvedb search API usage example
# ==============

import cvedb

cvedb_api = cvedb.Cvedb(api_key="YOUR_API_KEY_HERE")
possible_autocomplete = cvedb_api.autocomplete("heartbleed")
heartbleed_related = cvedb_api.search("heartbleed", limit=10)
total_heartbleed = heartbleed_related.total  # Notice you can do this because of Cvedb' own AttributeList type
CVE_2017_14174 = cvedb_api.document("CVE-2017-14174")
