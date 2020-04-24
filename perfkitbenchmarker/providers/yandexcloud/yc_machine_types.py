# Copyright 2020 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FLAVORS = [
    {
        'name': 'Micro',
        'memory': 1,
        'cores': 1
    },
    {
        'name': 'Small',
        'memory': 2,
        'cores': 1
    },
    {
        'name': 'Medium',
        'memory': 4,
        'cores': 2
    },
    {
        'name': 'Large',
        'memory': 8,
        'cores': 4
    },
    {
        'name': 'ExtraLarge',
        'memory': 16,
        'cores': 8
    },
    {
        'name': 'MemoryIntensiveSmall',
        'memory': 16,
        'cores': 2
    },
    {
        'name': 'MemoryIntensiveMedium',
        'memory': 32,
        'cores': 2
    },
    {
        'name': 'MemoryIntensiveLarge',
        'memory': 64,
        'cores': 2
    },
]