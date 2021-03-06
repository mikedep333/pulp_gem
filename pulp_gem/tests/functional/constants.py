# coding=utf-8
"""Constants for Pulp Gem plugin tests."""
from urllib.parse import urljoin

from pulp_smash.constants import PULP_FIXTURES_BASE_URL
from pulp_smash.pulp3.constants import (
    BASE_PUBLISHER_PATH,
    BASE_REMOTE_PATH,
    CONTENT_PATH
)


DOWNLOAD_POLICIES = ['immediate', 'streamed', 'on_demand']

GEM_CONTENT_NAME = 'gem.gem'

GEM_CONTENT_PATH = urljoin(CONTENT_PATH, 'gem/gems/')

GEM_REMOTE_PATH = urljoin(BASE_REMOTE_PATH, 'gem/gem/')

GEM_PUBLISHER_PATH = urljoin(BASE_PUBLISHER_PATH, 'gem/gem/')

# GEM_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'gem/')
GEM_FIXTURE_URL = 'https://repos.fedorapeople.org/pulp/pulp/demo_repos/gems/repo/'
"""The URL to a gem repository."""

GEM_FIXTURE_COUNT = 3
"""The number of content units available at :data:`GEM_FIXTURE_URL`."""

GEM_FIXTURE_SUMMARY = {
    GEM_CONTENT_NAME: GEM_FIXTURE_COUNT,
}
"""The desired content summary after syncing :data:`GEM_FIXTURE_URL`."""

GEM_URL = urljoin(GEM_FIXTURE_URL, 'gems/panda-0.1.0.gem')
"""The URL to an gem file at :data:`GEM_FIXTURE_URL`."""

# FIXME: replace this with your own fixture repository URL and metadata
GEM_INVALID_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'gem-invalid/')
"""The URL to an invalid gem repository."""

# FIXME: replace this with your own fixture repository URL and metadata
GEM_LARGE_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, 'gem-large/')
"""The URL to a gem repository containing a large number of content units."""

# FIXME: replace this with the actual number of content units in your test fixture
GEM_LARGE_FIXTURE_COUNT = 25
"""The number of content units available at :data:`GEM_LARGE_FIXTURE_URL`."""
