# -*- coding: utf-8 -*-
# Copyright 2015, 2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import synapse.metrics
from lrucache import LruCache

DEBUG_CACHES = False

metrics = synapse.metrics.get_metrics_for("synapse.util.caches")

caches_by_name = {}
cache_counter = metrics.register_cache(
    "cache",
    lambda: {(name,): len(caches_by_name[name]) for name in caches_by_name.keys()},
    labels=["name"],
)

_string_cache = LruCache(5000)
caches_by_name["string_cache"] = _string_cache


def intern_string(string):
    return _string_cache.setdefault(string, string)
