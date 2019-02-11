#!/usr/bin/env python3
# Copyright (C)2019 Lynnesbian (https://fedi.lynnesbian.space/@lynnesbian)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from mastodon import Mastodon

#fixtodon overrides a JSON parsing method used by mastodon.py that breaks pleroma support.
#specifically this function: https://github.com/halcy/Mastodon.py/blob/8b8626978752baf14347498640b2319db832145e/mastodon/Mastodon.py#L2110

#another issue not fixed by fixtodon: calling fetch_next will cause a crash if used on pleroma instances, so we're just not gonna use it ;)
#fetching things via activitypub's outbox.json is faster anyway

#thanks to jfmcbrayer - https://github.com/jfmcbrayer/Mastodon.py/commit/07853f241524ea965e796e0c8e1bf6dade63c2a9

class Fixtodon(Mastodon):
	@staticmethod
	def __json_strnum_to_bignum(self, json_object):
		raise AttributeError("dont use this uwu")

	@staticmethod
	def __json_hooks(self, json_object):
		json_object = Mastodon.__json_date_parse(json_object)
		json_object = Mastodon.__json_truefalse_parse(json_object)
		json_object = Mastodon.__json_allow_dict_attrs(json_object)
		return json_object
