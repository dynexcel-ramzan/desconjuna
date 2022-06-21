# -*- coding: utf-8 -*-
#################################################################################
# Author      : Dynexcel (<https://dynexcel.com/>)
# Copyright(c): 2015-Present dynexcel.com
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
#################################################################################
{
  "name"                 :  "Update Mrp production post inventory method",
  "summary"              :  "Update Mrp production post inventory method",
  "category"             :  "Manufacturing",
  "version"              :  "1.1",
  "sequence"             :  1,
  "author"               :  "Dynexcel",
  "license"              :  "AGPL-3",
  "website"              :  "http://dynexcel.co",
  "description"          :  """

""",
  "live_test_url"        :  "",
  "depends"              :  [
                             'base', 'mrp'
                            ],
  "data"                 :  [
                             'views/purchase_demand_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  0,
  "currency"             :  "EUR",
  "images"		 :['static/description/banner.jpg'],
}