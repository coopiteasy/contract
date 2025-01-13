# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class ContractContract(models.Model):
    _inherit = "contract.contract"

    def _prepare_recurring_sales_values(self, date_ref=False):
        res = super()._prepare_recurring_sales_values(date_ref)
        if res:
            res[0]["payment_mode_id"] = self.payment_mode_id.id
        return res
