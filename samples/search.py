#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cvedb search API usage example

import os

import cvedb

cvedb_api = cvedb.CvedbApi(api_key=os.environ["KEY"])
possible_autocomplete = cvedb_api.query_autocomplete("heartbleed")
heartbleed_related = cvedb_api.find("heartbleed", limit=10)
total_heartbleed = heartbleed_related.total
CVE_2017_14174 = cvedb_api.get_bulletin("CVE-2017-14174")
