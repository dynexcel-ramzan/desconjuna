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
  "name"                 :  "Show Reference and Agent Id Filter",
  "summary"              :  "Show Reference on invoice list view. Add reference and Agent name in quick search and group by in Invoices",
  "category"             :  "Accounting",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "Dynexcel",
  "license"              :  "AGPL-3",
  "website"              :  "http://dynexcel.com",
  "description"          :  """

""",
  "live_test_url"        :  "",
  "depends"              :  ['base', 'account', 'de_sale_comission'],
  "data"                 :  [
                             'views/account_move.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  0,
  "currency"             :  "EUR",
  "images"		 :['static/description/banner.jpg'],
}