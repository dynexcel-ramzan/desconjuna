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
  "name"                 :  "Sale Order on Packages",
  "summary"              :  "This modules add Sale order in stock packages",
  "category"             :  "Warehouse",
  "version"              :  "1.1",
  "sequence"             :  1,
  "author"               :  "Dynexcel",
  "license"              :  "Other proprietary",
  "website"              :  "http://dynexcel.com",
  "description"          :  """

""",
  "live_test_url"        :  "https://www.youtube.com/watch?v=YHKrxM8pHMw",
  "depends"              :  [
                             'base','stock',
                            ],
  "data"                 :  [
                            'views/stock_package_view.xml',

                            ],
  "images"               :  ['static/description/logo.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  19,
  "currency"             :  "EUR",
  "images"		 :['static/description/logo.png'],
}
